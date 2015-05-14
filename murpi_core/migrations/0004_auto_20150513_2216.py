# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('murpi_core', '0003_auto_20150512_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roleplay',
            name='status',
            field=models.CharField(max_length=2, choices=[(b'DV', b'In Development'), (b'OP', b'Open (Recruiting)'), (b'CL', b'Closed (Not Accepting Character Applications)'), (b'RO', b'Re-Open (Accepting New Characters)'), (b'FI', b'Finished'), (b'DD', b'Dead')]),
        ),
        migrations.DeleteModel(
            name='RoleplayStatus',
        ),
    ]
