# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('murpi_core', '0003_auto_20150519_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterRoleplayPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('owner', models.ForeignKey(to='murpi_core.Player')),
                ('roleplay', models.ForeignKey(to='murpi_core.Roleplay', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiscussionPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(related_name='ds_post_author', to='murpi_core.Player')),
                ('discussion', models.ForeignKey(to='murpi_core.Discussion')),
                ('modified_by', models.ForeignKey(related_name='ds_post_modified_by', to='murpi_core.Player', null=True)),
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
            ],
        ),
        migrations.RemoveField(
            model_name='characterpost',
            name='character',
        ),
        migrations.RemoveField(
            model_name='characterpost',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='character',
        ),
        migrations.RemoveField(
            model_name='post',
            name='scene',
        ),
        migrations.AddField(
            model_name='character',
            name='modified_by',
            field=models.ForeignKey(related_name='character_modified_by', to='murpi_core.Player', null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='author',
            field=models.ForeignKey(related_name='character_author', to='murpi_core.Player'),
        ),
        migrations.DeleteModel(
            name='CharacterPost',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='roleplaypost',
            name='character',
            field=models.ForeignKey(to='murpi_core.Character'),
        ),
        migrations.AddField(
            model_name='roleplaypost',
            name='modified_by',
            field=models.ForeignKey(related_name='rp_post_modified_by', to='murpi_core.Player', null=True),
        ),
        migrations.AddField(
            model_name='roleplaypost',
            name='scene',
            field=models.ForeignKey(to='murpi_core.Scene'),
        ),
        migrations.AddField(
            model_name='characterroleplaypost',
            name='character',
            field=models.ForeignKey(to='murpi_core.Character'),
        ),
        migrations.AddField(
            model_name='characterroleplaypost',
            name='post',
            field=models.ForeignKey(to='murpi_core.RoleplayPost'),
        ),
    ]
