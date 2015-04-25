# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badge_site', '0009_auto_20150422_1241'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='badge',
            options={'ordering': ['-created']},
        ),
        migrations.RemoveField(
            model_name='revocation',
            name='jsonfile',
        ),
        migrations.AddField(
            model_name='issuer',
            name='revocationfile',
            field=models.CharField(max_length=512, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='award',
            name='evidence',
            field=models.URLField(help_text=b'URL that points to a resource that provides evidence for this award.', max_length=1024),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='revocation',
            name='issuer',
            field=models.OneToOneField(related_name='revoked_list', to='badge_site.Issuer'),
            preserve_default=True,
        ),
    ]
