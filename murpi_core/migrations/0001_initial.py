# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
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
                ('file_name', models.CharField(max_length=10)),
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
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('background', models.ForeignKey(related_name='place_background', to='murpi_core.Photo', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=40)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('avatar', models.ForeignKey(to='murpi_core.Photo')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=100)),
                ('primary', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('player', models.ForeignKey(to='murpi_core.Player')),
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
                ('details', jsonfield.fields.JSONField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to='murpi_core.Player')),
            ],
        ),
        migrations.CreateModel(
            name='RoleplayStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
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
            model_name='roleplay',
            name='status',
            field=models.ForeignKey(to='murpi_core.RoleplayStatus'),
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
            name='race',
            field=models.ForeignKey(to='murpi_core.Race'),
        ),
        migrations.AddField(
            model_name='character',
            name='scene',
            field=models.ForeignKey(to='murpi_core.Scene', null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='status',
            field=models.ForeignKey(to='murpi_core.CharacterStatus'),
        ),
    ]
