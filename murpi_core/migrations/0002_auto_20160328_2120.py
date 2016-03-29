# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import murpi_core.models


class Migration(migrations.Migration):

    dependencies = [
        ('murpi_core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='height',
            new_name='image_height',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='width',
            new_name='image_width',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='height',
            new_name='image_height',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='width',
            new_name='image_width',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='height',
            new_name='image_height',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='width',
            new_name='image_width',
        ),
        migrations.RenameField(
            model_name='race',
            old_name='height',
            new_name='image_height',
        ),
        migrations.RenameField(
            model_name='race',
            old_name='width',
            new_name='image_width',
        ),
        migrations.RenameField(
            model_name='universe',
            old_name='height',
            new_name='image_height',
        ),
        migrations.RenameField(
            model_name='universe',
            old_name='width',
            new_name='image_width',
        ),
        migrations.RenameField(
            model_name='world',
            old_name='height',
            new_name='image_height',
        ),
        migrations.RenameField(
            model_name='world',
            old_name='width',
            new_name='image_width',
        ),
        migrations.AlterField(
            model_name='character',
            name='image',
            field=models.ImageField(height_field=b'image_height', width_field=b'image_width', upload_to=murpi_core.models.generate_image_path),
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(height_field=b'image_height', width_field=b'image_width', upload_to=murpi_core.models.generate_image_path),
        ),
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.ImageField(height_field=b'image_height', width_field=b'image_width', upload_to=murpi_core.models.generate_image_path),
        ),
        migrations.AlterField(
            model_name='race',
            name='image',
            field=models.ImageField(height_field=b'image_height', width_field=b'image_width', upload_to=murpi_core.models.generate_image_path),
        ),
        migrations.AlterField(
            model_name='universe',
            name='image',
            field=models.ImageField(height_field=b'image_height', width_field=b'image_width', upload_to=murpi_core.models.generate_image_path),
        ),
        migrations.AlterField(
            model_name='world',
            name='image',
            field=models.ImageField(height_field=b'image_height', width_field=b'image_width', upload_to=murpi_core.models.generate_image_path),
        ),
    ]
