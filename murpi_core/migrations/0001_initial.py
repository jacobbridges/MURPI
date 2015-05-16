# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
from django.conf import settings
import murpi_core.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('nick', models.CharField(max_length=100, null=True)),
                ('details', jsonfield.fields.JSONField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('character', models.ForeignKey(to='murpi_core.Character')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_name', models.ImageField(height_field=b'height', width_field=b'width', upload_to=murpi_core.models.generate_photo_path)),
                ('width', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('short_description', models.CharField(max_length=500, null=True)),
                ('description', models.TextField()),
                ('is_public', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('background', models.ForeignKey(related_name='place_background', to='murpi_core.Photo', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('avatar', models.ForeignKey(to='murpi_core.Photo')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to='murpi_core.Player')),
                ('character', models.ForeignKey(to='murpi_core.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=500, null=True)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to='murpi_core.Player')),
                ('thumbnail', models.ForeignKey(to='murpi_core.Photo')),
            ],
        ),
        migrations.CreateModel(
            name='Roleplay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=500, null=True)),
                ('description', models.TextField()),
                ('plain_rules', models.TextField(null=True)),
                ('is_public', models.BooleanField(default=False)),
                ('status', models.CharField(default=b'DV', max_length=2, choices=[(b'DV', b'In Development'), (b'OP', b'Open (Recruiting)'), (b'CL', b'Closed (Not Accepting Character Applications)'), (b'RO', b'Re-Open (Accepting New Characters)'), (b'FI', b'Finished'), (b'DD', b'Dead')])),
                ('details', jsonfield.fields.JSONField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to='murpi_core.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('short_description', models.CharField(max_length=500, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to='murpi_core.Player')),
                ('place', models.ForeignKey(to='murpi_core.Place')),
                ('roleplay', models.ForeignKey(to='murpi_core.Roleplay', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Universe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('short_description', models.CharField(max_length=500, null=True)),
                ('description', models.TextField()),
                ('is_public', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('background', models.ForeignKey(related_name='universe_background', to='murpi_core.Photo', null=True)),
                ('owner', models.ForeignKey(to='murpi_core.Player')),
                ('thumbnail', models.ForeignKey(related_name='universe_thumbnail', to='murpi_core.Photo')),
            ],
        ),
        migrations.CreateModel(
            name='World',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('short_description', models.CharField(max_length=500, null=True)),
                ('description', models.TextField()),
                ('is_public', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('background', models.ForeignKey(related_name='world_background', to='murpi_core.Photo', null=True)),
                ('owner', models.ForeignKey(to='murpi_core.Player')),
                ('thumbnail', models.ForeignKey(related_name='world_thumbnail', to='murpi_core.Photo')),
                ('universe', models.ForeignKey(to='murpi_core.Universe')),
            ],
        ),
        migrations.AddField(
            model_name='race',
            name='universe',
            field=models.ForeignKey(to='murpi_core.Universe'),
        ),
        migrations.AddField(
            model_name='post',
            name='scene',
            field=models.ForeignKey(to='murpi_core.Scene'),
        ),
        migrations.AddField(
            model_name='place',
            name='owner',
            field=models.ForeignKey(to='murpi_core.Player'),
        ),
        migrations.AddField(
            model_name='place',
            name='thumbnail',
            field=models.ForeignKey(related_name='place_thumbnail', to='murpi_core.Photo'),
        ),
        migrations.AddField(
            model_name='place',
            name='world',
            field=models.ForeignKey(to='murpi_core.World'),
        ),
        migrations.AddField(
            model_name='characterpost',
            name='post',
            field=models.ForeignKey(to='murpi_core.Post'),
        ),
        migrations.AddField(
            model_name='character',
            name='author',
            field=models.ForeignKey(to='murpi_core.Player'),
        ),
        migrations.AddField(
            model_name='character',
            name='avatar',
            field=models.ForeignKey(to='murpi_core.Photo'),
        ),
        migrations.AddField(
            model_name='character',
            name='home_world',
            field=models.ForeignKey(to='murpi_core.World'),
        ),
        migrations.AddField(
            model_name='character',
            name='latest_scene',
            field=models.ForeignKey(to='murpi_core.Scene', null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.ForeignKey(to='murpi_core.Race'),
        ),
        migrations.AddField(
            model_name='character',
            name='status',
            field=models.ForeignKey(to='murpi_core.CharacterStatus'),
        ),
    ]
