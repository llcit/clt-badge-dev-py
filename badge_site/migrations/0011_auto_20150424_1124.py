# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badge_site', '0010_auto_20150424_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revocation',
            name='award',
            field=models.ForeignKey(to='badge_site.Award', unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='revocation',
            name='issuer',
            field=models.OneToOneField(related_name='revocations', to='badge_site.Issuer'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='revocation',
            unique_together=set([]),
        ),
    ]
