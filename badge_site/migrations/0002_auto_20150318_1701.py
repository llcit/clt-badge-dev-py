# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badge_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuer',
            name='guid',
            field=models.CharField(help_text=b'This is auto generated.', unique=True, max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
