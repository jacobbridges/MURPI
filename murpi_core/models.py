from django.db import models
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from jsonfield import JSONField
import hashlib
import time

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


def generate_avatar_path(instance, filename):
    """
    Generate new photo filename and path.
    Photo will be uploaded to MEDIA_ROOT/img/avatar/<hash>.<ext>
    """
    return 'img/avatar/{0}.{1}'.format(generate_hash(), filename.split('.')[-1])


def generate_thumbnail_path(instance, filename):
    """
    Generate new photo filename and path.
    Photo will be uploaded to MEDIA_ROOT/img/avatar/<hash>.<ext>
    """
    return 'img/thumbnail/{0}.{1}'.format(generate_hash(), filename.split('.')[-1])


def generate_background_path(instance, filename):
    """
    Generate new photo filename and path.
    Photo will be uploaded to MEDIA_ROOT/img/avatar/<hash>.<ext>
    """
    return 'img/background/{0}.{1}'.format(generate_hash(), filename.split('.')[-1])


# === Models for MURPI_core ===

# Not adding the verbose documentation to each model until there is a working core.


class Player(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to=generate_avatar_path, width_field='avatar_width', height_field='avatar_height')
    avatar_width = models.FloatField(null=True)
    avatar_height = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user.username


# A collection of scenes depicting a complete story
class Roleplay(models.Model):
    name = models.CharField(max_length=100, blank=False)
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
    details = JSONField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


# Universe -> World -> Place -> Scene
class Universe(models.Model):
    name = models.CharField(max_length=40, blank=False)
    short_description = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=False)
    owner = models.ForeignKey(Player)
    is_public = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to=generate_thumbnail_path, width_field='thumbnail_width', height_field='thumbnail_height')
    thumbnail_width = models.FloatField(null=True)
    thumbnail_height = models.FloatField(null=True)
    background = models.ImageField(upload_to=generate_background_path, null=True, width_field='background_width', height_field='background_height')
    background_width = models.FloatField(null=True)
    background_height = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


# World -> Place -> Scene
class World(models.Model):
    name = models.CharField(max_length=40, blank=False)
    short_description = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=False)
    owner = models.ForeignKey(Player)
    is_public = models.BooleanField(default=True)
    universe = models.ForeignKey(Universe)
    thumbnail = models.ImageField(upload_to=generate_thumbnail_path, width_field='thumbnail_width', height_field='thumbnail_height')
    thumbnail_width = models.FloatField(null=True)
    thumbnail_height = models.FloatField(null=True)
    background = models.ImageField(upload_to=generate_background_path, null=True, width_field='background_width', height_field='background_height')
    background_width = models.FloatField(null=True)
    background_height = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


# Place -> Scene
class Place(models.Model):
    name = models.CharField(max_length=40, blank=False)
    short_description = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=False)
    owner = models.ForeignKey(Player)
    world = models.ForeignKey(World)
    is_public = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to=generate_thumbnail_path, width_field='thumbnail_width', height_field='thumbnail_height')
    thumbnail_width = models.FloatField(null=True)
    thumbnail_height = models.FloatField(null=True)
    background = models.ImageField(upload_to=generate_background_path, null=True, width_field='background_width', height_field='background_height')
    background_width = models.FloatField(null=True)
    background_height = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Scene(models.Model):
    name = models.CharField(max_length=40, blank=False)
    short_description = models.CharField(max_length=500, null=True)
    owner = models.ForeignKey(Player)
    place = models.ForeignKey(Place)
    roleplay = models.ForeignKey(Roleplay, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Race(models.Model):
    name = models.CharField(max_length=50)
    universe = models.ForeignKey(Universe)
    short_description = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=False)
    owner = models.ForeignKey(Player)
    thumbnail = models.ImageField(upload_to=generate_thumbnail_path, width_field='thumbnail_width', height_field='thumbnail_height')
    thumbnail_width = models.FloatField(null=True)
    thumbnail_height = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class CharacterStatus(models.Model):
    name = models.CharField(max_length=40)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=100, blank=False)
    nick = models.CharField(max_length=100, null=True)
    race = models.ForeignKey(Race, blank=False)
    status = models.ForeignKey(CharacterStatus)
    avatar = models.ImageField(upload_to=generate_avatar_path, width_field='avatar_width', height_field='avatar_height')
    avatar_width = models.FloatField(null=True)
    avatar_height = models.FloatField(null=True)
    home_world = models.ForeignKey(World, blank=False)
    description = models.TextField(null=True)
    author = models.ForeignKey(Player, related_name='character_author')
    details = JSONField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Player, null=True, related_name='character_modified_by')

    def __unicode__(self):
        return self.name


class RoleplayPost(models.Model):
    text = models.TextField(blank=False)
    author = models.ForeignKey(Player, related_name='rp_post_author')
    character = models.ForeignKey(Character)
    scene = models.ForeignKey(Scene)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Player, null=True, related_name='rp_post_modified_by')

    def __unicode__(self):
        return "{} words posted by {} in {}".format(len(self.text.split()), self.author.user.username, self.scene.name)


# Which characters are referenced in a roleplay post?
class CharacterRoleplayPost(models.Model):
    character = models.ForeignKey(Character)
    post = models.ForeignKey(RoleplayPost)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "ch {} -> po {}".format(self.character_id, self.post_id)


class Discussion(models.Model):
    name = models.CharField(max_length=100, blank=False)
    owner = models.ForeignKey(Player)
    status = models.CharField(max_length=2, choices=(
        ('OP', 'Open'),
        ('LK', 'Locked'),
        ('CL', 'Closed')
    ), default='OP')
    roleplay = models.ForeignKey(Roleplay, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{}'s {} discussion for {}".format(self.owner.user.username, self.status, self.roleplay.name)


class DiscussionPost(models.Model):
    text = models.TextField(blank=False)
    author = models.ForeignKey(Player, related_name='ds_post_author')
    discussion = models.ForeignKey(Discussion)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Player, null=True, related_name='ds_post_modified_by')

    def __unicode__(self):
        return "{} words posted by {} in {}".format(len(self.text.split()), self.author.user.username, self.discussion.name)


# === Model Permissions ===

# Can create universes
# Permission.objects.create(codename='can_create_universe',
#                           name='Can Create Universe',
#                           content_type=ContentType.objects.get_for_model(Universe))

# Can create worlds
# Permission.objects.create(codename='can_create_world',
#                         name='Can Create World',
#                         content_type=ContentType.objects.get_for_model(World))