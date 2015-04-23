# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('badge_site', '0006_auto_20150323_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='revocation',
            name='revoke_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 24, 0, 14, 47, 135642, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
