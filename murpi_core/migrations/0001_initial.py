# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import murpi_core.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(height_field=b'height', width_field=b'width', upload_to=murpi_core.models.generate_image_path)),
                ('width', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('nick', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CharacterStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CharacterToRoleplayPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('character', models.ForeignKey(to='murpi_core.Character')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(default=b'OP', max_length=2, choices=[(b'OP', b'Open'), (b'LK', b'Locked'), (b'PN', b'Pinned'), (b'CL', b'Closed')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DiscussionPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(height_field=b'height', width_field=b'width', upload_to=murpi_core.models.generate_image_path)),
                ('width', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=500, null=True)),
                ('description', models.TextField()),
                ('is_public', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(height_field=b'height', width_field=b'width', upload_to=murpi_core.models.generate_image_path)),
                ('width', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(height_field=b'height', width_field=b'width', upload_to=murpi_core.models.generate_image_path)),
                ('width', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=500, null=True)),
                ('description', models.TextField()),
                ('owner', models.ForeignKey(to='murpi_core.Player')),
            ],
            options={
                'abstract': False,
            },
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
                ('game_master', models.ForeignKey(to='murpi_core.Player')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoleplayPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('author', models.ForeignKey(related_name='rp_post_author', to='murpi_core.Player')),
                ('character', models.ForeignKey(to='murpi_core.Character')),
                ('modified_by', models.ForeignKey(related_name='rp_post_modified_by', to='murpi_core.Player', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=500, null=True)),
                ('owner', models.ForeignKey(to='murpi_core.Player')),
                ('place', models.ForeignKey(to='murpi_core.Place')),
                ('roleplay', models.ForeignKey(to='murpi_core.Roleplay', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Universe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(height_field=b'height', width_field=b'width', upload_to=murpi_core.models.generate_image_path)),
                ('width', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=500, null=True)),
                ('description', models.TextField()),
                ('is_public', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(to='murpi_core.Player')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='World',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(height_field=b'height', width_field=b'width', upload_to=murpi_core.models.generate_image_path)),
                ('width', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=500, null=True)),
                ('description', models.TextField()),
                ('is_public', models.BooleanField(default=True)),
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
            model_name='charactertoroleplaypost',
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
        migrations.AlterUniqueTogether(
            name='world',
            unique_together=set([('name', 'universe')]),
        ),
        migrations.AlterUniqueTogether(
            name='scene',
            unique_together=set([('name', 'roleplay', 'place')]),
        ),
        migrations.AlterUniqueTogether(
            name='place',
            unique_together=set([('name', 'world')]),
        ),
    ]
