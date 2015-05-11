from django.db import models
from jsonfield import JSONField

# === Models for MURPI_core ===

# Not adding the verbose documentation to each model until there is a working core.


class Photo(models.Model):
    file_name = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Player(models.Model):
    name = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=40, blank=False)
    avatar = models.ForeignKey(Photo)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class PlayerEmail(models.Model):
    player = models.ForeignKey(Player)
    email = models.CharField(max_length=100, blank=False)
    primary = models.BooleanField(default=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


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


# World -> Place -> Scene
class World(models.Model):
    name = models.CharField(max_length=40, blank=False)
    short_description = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=False)
    owner = models.ForeignKey(Player, null=False)
    universe = models.ForeignKey(Universe, null=False)
    thumbnail = models.ForeignKey(Photo, related_name='world_thumbnail')
    background = models.ForeignKey(Photo, related_name='world_background', null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


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


class Scene(models.Model):
    name = models.CharField(max_length=40, blank=False)
    short_description = models.CharField(max_length=500, null=True)
    owner = models.ForeignKey(Player, null=False)
    place = models.ForeignKey(Place, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class RoleplayStatus(models.Model):
    name = models.CharField(max_length=40)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


# A collection of scenes depicting a complete story
class Roleplay(models.Model):
    name = models.CharField(max_length=100, blank=False)
    short_description = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=False)
    owner = models.ForeignKey(Player, null=False)
    plain_rules = models.TextField(null=True)
    is_public = models.BooleanField(default=False, null=False)
    status = models.ForeignKey(RoleplayStatus, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Race(models.Model):
    name = models.CharField(max_length=50)
    universe = models.ForeignKey(Universe, null=False)
    short_description = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=False)
    owner = models.ForeignKey(Player, null=False)
    thumbnail = models.ForeignKey(Photo)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Class(models.Model):
    name = models.CharField(max_length=50)
    race = models.ForeignKey(Race, null=True)
    description = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Mastery(models.Model):
    name = models.name = models.CharField(max_length=50)
    race = models.ForeignKey(Race, null=True)
    description = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Ability(models.Model):
    name = models.name = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Skill(models.Model):
    name = models.name = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Trait(models.Model):
    name = models.name = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class CharacterStatus(models.Model):
    name = models.CharField(max_length=40)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Character(models.Model):
    name = models.CharField(max_length=100, blank=False)
    nick = models.CharField(max_length=100, null=True)
    race = models.ForeignKey(Race, blank=False)
    primary_class = models.ForeignKey(Class, related_name='primary_class',  blank=False)
    secondary_class = models.ForeignKey(Class, related_name='secondary_class')
    status = models.ForeignKey(CharacterStatus)
    avatar = models.ForeignKey(Photo)
    home_world = models.ForeignKey(World, blank=False)
    scene = models.ForeignKey(Scene, null=True)
    details = JSONField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class CharacterTraits(models.Model):
    character = models.ForeignKey(Character, null=False)
    trait = models.ForeignKey(Trait, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class CharacterSkills(models.Model):
    character = models.ForeignKey(Character, null=False)
    skill = models.ForeignKey(Skill, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class CharacterAbilities(models.Model):
    character = models.ForeignKey(Character, null=False)
    ability = models.ForeignKey(Ability, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Post(models.Model):
    text = models.TextField(blank=False)
    author = models.ForeignKey(Player, null=False)
    character = models.ForeignKey(Character, null=False)
    scene = models.ForeignKey(Scene, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


# Which characters are referenced in this post?
class CharacterPost(models.Model):
    character = models.ForeignKey(Character, null=False)
    post = models.ForeignKey(Post, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


