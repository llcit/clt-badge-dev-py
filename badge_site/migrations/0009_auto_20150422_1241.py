# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badge_site', '0008_revocation_jsonfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='notification_status',
            field=models.DateField(default=None, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='badge',
            name='notify_email_message',
            field=models.TextField(default=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='badge',
            name='notify_email_subject',
            field=models.CharField(default=b'', max_length=256, blank=True),
            preserve_default=True,
        ),
    ]
