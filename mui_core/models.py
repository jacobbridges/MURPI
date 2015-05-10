from django.db import models


class Avatar(models.Model):
    file_name = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Player(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=30)
    avatar = models.ForeignKey(Avatar)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
