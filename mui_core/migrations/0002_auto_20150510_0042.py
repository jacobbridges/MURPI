# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mui_core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='avatar_id',
            new_name='avatar',
        ),
    ]
