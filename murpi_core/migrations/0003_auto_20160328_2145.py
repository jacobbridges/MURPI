# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('murpi_core', '0002_auto_20160328_2120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='author',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='character',
            name='nick',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
