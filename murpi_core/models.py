from django.db import models
from django.contrib.auth.models import User
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


def generate_photo_path(instance, filename):
    """
    Generate new photo filename and path.
    Photo will be uploaded to MEDIA_ROOT/img/avatar/<hash>.<ext>
    """
    return 'img/avatar/{0}.{1}'.format(generate_hash(), instance.file_extension)


# === Models for MURPI_core ===

# Not adding the verbose documentation to each model until there is a working core.


class Photo(models.Model):
    file_name = models.ImageField(upload_to=generate_photo_path, width_field='width', height_field='height')
    width = models.FloatField(null=True)
    height = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.file_name.url


class Player(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ForeignKey(Photo)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.user.username


# A collection of scenes depicting a complete story
class Roleplay(models.Model):
    name = models.CharField(max_length=100, blank=False)
    short_description = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=False)
    owner = models.ForeignKey(Player)
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
    owner = models.ForeignKey(Player, null=False)
    is_public = models.BooleanField(default=True, null=False)
    thumbnail = models.ForeignKey(Photo, related_name='universe_thumbnail')
    background = models.ForeignKey(Photo, related_name='universe_background', null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


# World -> Place -> Scene
class World(models.Model):
    name = models.CharField(max_length=40, blank=False)
    short_description = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=False)
    owner = models.ForeignKey(Player, null=False)
    is_public = models.BooleanField(default=True, null=False)
    universe = models.ForeignKey(Universe, null=False)
    thumbnail = models.ForeignKey(Photo, related_name='world_thumbnail')
    background = models.ForeignKey(Photo, related_name='world_background', null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


# Place -> Scene
class Place(models.Model):
    name = models.CharField(max_length=40, blank=False)
    short_description = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=False)
    owner = models.ForeignKey(Player, null=False)
    world = models.ForeignKey(World, null=False)
    is_public = models.BooleanField(default=True, null=False)
    thumbnail = models.ForeignKey(Photo, related_name='place_thumbnail')
    background = models.ForeignKey(Photo, related_name='place_background', null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Scene(models.Model):
    name = models.CharField(max_length=40, blank=False)
    short_description = models.CharField(max_length=500, null=True)
    owner = models.ForeignKey(Player, null=False)
    place = models.ForeignKey(Place, null=False)
    roleplay = models.ForeignKey(Roleplay, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Race(models.Model):
    name = models.CharField(max_length=50)
    universe = models.ForeignKey(Universe, null=False)
    short_description = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=False)
    owner = models.ForeignKey(Player, null=False)
    thumbnail = models.ForeignKey(Photo)
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
    avatar = models.ForeignKey(Photo)
    home_world = models.ForeignKey(World, blank=False)
    author = models.ForeignKey(Player, null=False)
    latest_scene = models.ForeignKey(Scene, null=True)
    details = JSONField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    text = models.TextField(blank=False)
    author = models.ForeignKey(Player, null=False)
    character = models.ForeignKey(Character, null=False)
    scene = models.ForeignKey(Scene, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{} words posted by {} in {}".format(len(self.text.split()), self.author.name, self.scene.name)


# Which characters are referenced in this post?
class CharacterPost(models.Model):
    character = models.ForeignKey(Character, null=False)
    post = models.ForeignKey(Post, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "ch {} -> po {}".format(self.character_id, self.post_id)