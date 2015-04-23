# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badge_site', '0005_auto_20150323_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.CharField(max_length=512)),
                ('award', models.ForeignKey(to='badge_site.Award')),
                ('issuer', models.ForeignKey(related_name='revoked_ist', to='badge_site.Issuer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='revocations',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='revocations',
            name='award',
        ),
        migrations.RemoveField(
            model_name='revocations',
            name='issuer',
        ),
        migrations.DeleteModel(
            name='Revocations',
        ),
        migrations.AlterUniqueTogether(
            name='revocation',
            unique_together=set([('issuer', 'award')]),
        ),
    ]
