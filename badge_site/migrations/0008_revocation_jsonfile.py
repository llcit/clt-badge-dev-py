# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badge_site', '0007_revocation_revoke_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='revocation',
            name='jsonfile',
            field=models.URLField(help_text=b'This is auto generated but is fully qualified url for the revocation list.', max_length=1024, blank=True),
            preserve_default=True,
        ),
    ]
