from django.db import models
from murpi_core.models import Race, Character


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