# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('murpi_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='roleplay',
            field=models.ForeignKey(to='murpi_core.Roleplay', null=True),
        ),
    ]
