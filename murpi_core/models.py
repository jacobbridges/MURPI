from django.db import models
from jsonfield import JSONField
import hashlib
import time

# === Methods for MURPI_core models ===

# To reset migrations
# ./manage.py migrate --fake murpi_core zero


def generate_hash_10():
        """This function generate 10 character long hash"""
        full_hash = hashlib.sha1()
        full_hash.update(str(time.time()))
        return full_hash.hexdigest()[:-10]

# === Models for MURPI_core ===

# Not adding the verbose documentation to each model until there is a working core.


class Photo(models.Model):
    file_name = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.file_name


class Player(models.Model):
    name = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=40, blank=False)
    avatar = models.ForeignKey(Photo)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class PlayerEmail(models.Model):
    player = models.ForeignKey(Player)
    email = models.CharField(max_length=100, blank=False)
    primary = models.BooleanField(default=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.email


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
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class RoleplayStatus(models.Model):
    name = models.CharField(max_length=40)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


# A collection of scenes depicting a complete story
class Roleplay(models.Model):
    name = models.CharField(max_length=100, blank=False)
    short_description = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=False)
    owner = models.ForeignKey(Player, null=False)
    plain_rules = models.TextField(null=True)
    is_public = models.BooleanField(default=False, null=False)
    status = models.ForeignKey(RoleplayStatus, null=False)
    details = JSONField(null=True)
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
    scene = models.ForeignKey(Scene, null=True)
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