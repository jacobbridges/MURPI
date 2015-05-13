# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import murpi_core.models


class Migration(migrations.Migration):

    dependencies = [
        ('murpi_core', '0002_auto_20150511_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='height',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='width',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='file_name',
            field=models.ImageField(height_field=b'height', width_field=b'width', upload_to=murpi_core.models.generate_photo_path),
        ),
    ]
