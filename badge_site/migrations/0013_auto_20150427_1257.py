# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badge_site', '0012_auto_20150424_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='jsonfile_name',
            field=models.CharField(max_length=512, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='badge',
            name='jsonfile_name',
            field=models.CharField(max_length=512, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='issuer',
            name='jsonfile_name',
            field=models.CharField(max_length=512, null=True, blank=True),
            preserve_default=True,
        ),
    ]
