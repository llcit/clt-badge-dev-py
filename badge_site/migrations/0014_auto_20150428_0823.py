# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badge_site', '0013_auto_20150427_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='created',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
