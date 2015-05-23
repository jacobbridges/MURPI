# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import murpi_core.models


class Migration(migrations.Migration):

    dependencies = [
        ('murpi_core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='background',
            field=models.ImageField(default=b'settings.MEDIA_ROOT/img/background/default.jpg', height_field=b'background_height', width_field=b'background_width', null=True, upload_to=murpi_core.models.generate_background_path),
        ),
        migrations.AlterField(
            model_name='universe',
            name='background',
            field=models.ImageField(default=b'settings.MEDIA_ROOT/img/background/default.jpg', height_field=b'background_height', width_field=b'background_width', null=True, upload_to=murpi_core.models.generate_background_path),
        ),
        migrations.AlterField(
            model_name='world',
            name='background',
            field=models.ImageField(default=b'settings.MEDIA_ROOT/img/background/default.jpg', height_field=b'background_height', width_field=b'background_width', null=True, upload_to=murpi_core.models.generate_background_path),
        ),
        migrations.AlterUniqueTogether(
            name='place',
            unique_together=set([('name', 'world')]),
        ),
        migrations.AlterUniqueTogether(
            name='world',
            unique_together=set([('name', 'universe')]),
        ),
    ]
