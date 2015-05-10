from django.db import models


class Avatar(models.Model):
    file_name = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Player(models.Model):
    name = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=40, blank=False)
    avatar = models.ForeignKey(Avatar)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
