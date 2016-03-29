from django.db import models
from django.contrib.auth.models import User

import hashlib
import time

from toolz import curry

# === Methods for MURPI_core models ===

# To reset migrations
# ./manage.py migrate --fake murpi_core zero


def generate_hash():
    """
    Generate a unique hash based on the current time
    """
    full_hash = hashlib.sha1()
    full_hash.update(str(time.time()))
    return full_hash.hexdigest()


def generate_image_path(instance, filename):
    """
    Generate new image filename and path.
    Photo will be uploaded to MEDIA_ROOT/<category>/<hash>.<ext>
    """
    return 'img/{category}{hash}.{ext}'.format(
        category=generate_image_path.category + '/',
        hash=generate_hash(),
        ext=filename.split('.')[-1]
    )
generate_image_path.category = 'avatar'


# === Models for MURPI_core ===

# Not adding the verbose documentation to each model until there is a working core.


class MModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ModelWithImage(models.Model):
    _category = 'avatar'
    generate_image_path.category = _category

    image = models.ImageField(upload_to=generate_image_path, width_field='image_width', height_field='image_height')
    image_width = models.FloatField(null=True)
    image_height = models.FloatField(null=True)

    class Meta:
        abstract = True

    @classmethod
    def has_file(cls, file_path):
        return True if cls.objects.filter(image=file_path) else False


class ModelWithName(models.Model):
    name = models.CharField(max_length=100, blank=False)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name


class Player(MModel, ModelWithImage):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username


# A collection of scenes depicting a complete story
class Roleplay(ModelWithName):
    short_description = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=False)
    game_master = models.ForeignKey(Player)
    plain_rules = models.TextField(null=True)
    is_public = models.BooleanField(default=False)
    status = models.CharField(max_length=2, choices=(
        ('DV', 'In Development'),
        ('OP', 'Open (Recruiting)'),
        ('CL', 'Closed (Not Accepting Character Applications)'),
        ('RO', 'Re-Open (Accepting New Characters)'),
        ('FI', 'Finished'),
        ('DD', 'Dead')
    ), default='DV')


# Universe -> World -> Place -> Scene
class Universe(MModel, ModelWithImage, ModelWithName):
    short_description = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=False)
    owner = models.ForeignKey(Player)
    is_public = models.BooleanField(default=True)

    _category = 'background'


# World -> Place -> Scene
class World(MModel, ModelWithImage, ModelWithName):
    short_description = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=False)
    owner = models.ForeignKey(Player)
    is_public = models.BooleanField(default=True)
    universe = models.ForeignKey(Universe)

    _category = 'background'

    class Meta:
        unique_together = ('name', 'universe',)


# Place -> Scene
class Place(MModel, ModelWithImage, ModelWithName):
    short_description = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=False)
    owner = models.ForeignKey(Player)
    world = models.ForeignKey(World)
    is_public = models.BooleanField(default=True)

    _category = 'background'

    class Meta:
        unique_together = ('name', 'world',)


class Scene(MModel, ModelWithName):
    short_description = models.CharField(max_length=500, null=True)
    owner = models.ForeignKey(Player)
    place = models.ForeignKey(Place)
    roleplay = models.ForeignKey(Roleplay, null=True)

    class Meta:
        unique_together = (('name', 'roleplay', 'place'),)


class Race(MModel, ModelWithImage, ModelWithName):
    universe = models.ForeignKey(Universe)
    short_description = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=False)
    owner = models.ForeignKey(Player)

    _category = 'avatar'


class CharacterStatus(ModelWithName):
    pass


class Character(MModel, ModelWithImage, ModelWithName):
    nick = models.CharField(max_length=100, blank=True, null=True)
    race = models.ForeignKey(Race, blank=False)
    status = models.ForeignKey(CharacterStatus)
    home_world = models.ForeignKey(World, blank=False)
    description = models.TextField(null=True)
    owner = models.ForeignKey(Player, related_name='character_author')
    modified_by = models.ForeignKey(Player, null=True, related_name='character_modified_by')

    _category = 'avatar'


class RoleplayPost(MModel):
    text = models.TextField(blank=False)
    author = models.ForeignKey(Player, related_name='rp_post_author')
    character = models.ForeignKey(Character)
    scene = models.ForeignKey(Scene)
    modified_by = models.ForeignKey(Player, null=True, related_name='rp_post_modified_by')

    def __unicode__(self):
        return "{} words posted by {} in {}".format(len(self.text.split()), self.author.user.username, self.scene.name)


# Which characters are referenced in a roleplay post?
class CharacterToRoleplayPost(MModel):
    character = models.ForeignKey(Character)
    post = models.ForeignKey(RoleplayPost)

    def __unicode__(self):
        return "ch {} -> po {}".format(self.character_id, self.post_id)


class Discussion(MModel, ModelWithName):
    owner = models.ForeignKey(Player)
    status = models.CharField(max_length=2, choices=(
        ('OP', 'Open'),
        ('LK', 'Locked'),
        ('PN', 'Pinned'),
        ('CL', 'Closed'),
    ), default='OP')
    roleplay = models.ForeignKey(Roleplay, null=True)

    def __unicode__(self):
        return "{}'s {} discussion for {}".format(self.owner.user.username, self.status, self.roleplay.name)


class DiscussionPost(MModel):
    text = models.TextField(blank=False)
    author = models.ForeignKey(Player, related_name='ds_post_author')
    discussion = models.ForeignKey(Discussion)
    modified_by = models.ForeignKey(Player, null=True, related_name='ds_post_modified_by')

    def __unicode__(self):
        return "{} words posted by {} in {}".format(len(self.text.split()), self.author.user.username, self.discussion.name)


# === Model Permissions ===

# from django.contrib.auth.models import Group, Permission
# from django.contrib.contenttypes.models import ContentType

# Can create universes
# Permission.objects.create(codename='can_create_universe',
#                           name='Can Create Universe',
#                           content_type=ContentType.objects.get_for_model(Universe))

# Can create worlds
# Permission.objects.create(codename='can_create_world',
#                         name='Can Create World',
#                         content_type=ContentType.objects.get_for_model(World))
