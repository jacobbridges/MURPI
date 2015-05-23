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
                ('avatar', models.ImageField(height_field=b'avatar_height', width_field=b'avatar_width', upload_to=murpi_core.models.generate_avatar_path)),
                ('avatar_width', models.FloatField(null=True)),
                ('avatar_height', models.FloatField(null=True)),
                ('description', models.TextField(null=True)),
                ('details', jsonfield.fields.JSONField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterRoleplayPost',
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
            name='Discussion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(default=b'OP', max_length=2, choices=[(b'OP', b'Open'), (b'LK', b'Locked'), (b'CL', b'Closed')])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiscussionPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
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
                ('thumbnail', models.ImageField(height_field=b'thumbnail_height', width_field=b'thumbnail_width', upload_to=murpi_core.models.generate_thumbnail_path)),
                ('thumbnail_width', models.FloatField(null=True)),
                ('thumbnail_height', models.FloatField(null=True)),
                ('background', models.ImageField(height_field=b'background_height', width_field=b'background_width', null=True, upload_to=murpi_core.models.generate_background_path)),
                ('background_width', models.FloatField(null=True)),
                ('background_height', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(height_field=b'avatar_height', width_field=b'avatar_width', upload_to=murpi_core.models.generate_avatar_path)),
                ('avatar_width', models.FloatField(null=True)),
                ('avatar_height', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=500, null=True)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(height_field=b'thumbnail_height', width_field=b'thumbnail_width', upload_to=murpi_core.models.generate_thumbnail_path)),
                ('thumbnail_width', models.FloatField(null=True)),
                ('thumbnail_height', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to='murpi_core.Player')),
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
                ('game_master', models.ForeignKey(to='murpi_core.Player')),
            ],
        ),
        migrations.CreateModel(
            name='RoleplayPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(related_name='rp_post_author', to='murpi_core.Player')),
                ('character', models.ForeignKey(to='murpi_core.Character')),
                ('modified_by', models.ForeignKey(related_name='rp_post_modified_by', to='murpi_core.Player', null=True)),
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
                ('thumbnail', models.ImageField(height_field=b'thumbnail_height', width_field=b'thumbnail_width', upload_to=murpi_core.models.generate_thumbnail_path)),
                ('thumbnail_width', models.FloatField(null=True)),
                ('thumbnail_height', models.FloatField(null=True)),
                ('background', models.ImageField(height_field=b'background_height', width_field=b'background_width', null=True, upload_to=murpi_core.models.generate_background_path)),
                ('background_width', models.FloatField(null=True)),
                ('background_height', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to='murpi_core.Player')),
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
                ('thumbnail', models.ImageField(height_field=b'thumbnail_height', width_field=b'thumbnail_width', upload_to=murpi_core.models.generate_thumbnail_path)),
                ('thumbnail_width', models.FloatField(null=True)),
                ('thumbnail_height', models.FloatField(null=True)),
                ('background', models.ImageField(height_field=b'background_height', width_field=b'background_width', null=True, upload_to=murpi_core.models.generate_background_path)),
                ('background_width', models.FloatField(null=True)),
                ('background_height', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to='murpi_core.Player')),
                ('universe', models.ForeignKey(to='murpi_core.Universe')),
            ],
        ),
        migrations.AddField(
            model_name='roleplaypost',
            name='scene',
            field=models.ForeignKey(to='murpi_core.Scene'),
        ),
        migrations.AddField(
            model_name='race',
            name='universe',
            field=models.ForeignKey(to='murpi_core.Universe'),
        ),
        migrations.AddField(
            model_name='place',
            name='owner',
            field=models.ForeignKey(to='murpi_core.Player'),
        ),
        migrations.AddField(
            model_name='place',
            name='world',
            field=models.ForeignKey(to='murpi_core.World'),
        ),
        migrations.AddField(
            model_name='discussionpost',
            name='author',
            field=models.ForeignKey(related_name='ds_post_author', to='murpi_core.Player'),
        ),
        migrations.AddField(
            model_name='discussionpost',
            name='discussion',
            field=models.ForeignKey(to='murpi_core.Discussion'),
        ),
        migrations.AddField(
            model_name='discussionpost',
            name='modified_by',
            field=models.ForeignKey(related_name='ds_post_modified_by', to='murpi_core.Player', null=True),
        ),
        migrations.AddField(
            model_name='discussion',
            name='owner',
            field=models.ForeignKey(to='murpi_core.Player'),
        ),
        migrations.AddField(
            model_name='discussion',
            name='roleplay',
            field=models.ForeignKey(to='murpi_core.Roleplay', null=True),
        ),
        migrations.AddField(
            model_name='characterroleplaypost',
            name='post',
            field=models.ForeignKey(to='murpi_core.RoleplayPost'),
        ),
        migrations.AddField(
            model_name='character',
            name='author',
            field=models.ForeignKey(related_name='character_author', to='murpi_core.Player'),
        ),
        migrations.AddField(
            model_name='character',
            name='home_world',
            field=models.ForeignKey(to='murpi_core.World'),
        ),
        migrations.AddField(
            model_name='character',
            name='modified_by',
            field=models.ForeignKey(related_name='character_modified_by', to='murpi_core.Player', null=True),
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
