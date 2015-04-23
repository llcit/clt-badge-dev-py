# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badge_site', '0002_auto_20150318_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuer',
            name='guid',
            field=models.CharField(help_text=b'This is auto generated and cannot be edited.', unique=True, max_length=10, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='issuer',
            name='jsonfile',
            field=models.URLField(max_length=1024, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
