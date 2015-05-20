# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('murpi_core', '0002_auto_20150519_1923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roleplay',
            old_name='owner',
            new_name='game_master',
        ),
    ]
