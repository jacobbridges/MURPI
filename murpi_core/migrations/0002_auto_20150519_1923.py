# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('murpi_core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='latest_scene',
        ),
        migrations.AddField(
            model_name='character',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
