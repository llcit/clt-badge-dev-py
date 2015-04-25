# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badge_site', '0011_auto_20150424_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revocation',
            name='issuer',
            field=models.ForeignKey(related_name='revocations', to='badge_site.Issuer'),
            preserve_default=True,
        ),
    ]
