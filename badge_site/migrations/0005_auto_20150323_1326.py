# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('badge_site', '0004_auto_20150318_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revocations',
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
            unique_together=set([('issuer', 'award')]),
        ),
        migrations.AlterField(
            model_name='award',
            name='badge',
            field=models.ForeignKey(related_name='awards', to='badge_site.Badge'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='award',
            name='guid',
            field=models.CharField(help_text=b'This is auto generated.', unique=True, max_length=24),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='badge',
            name='guid',
            field=models.CharField(unique=True, max_length=24),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='badge',
            name='issuer',
            field=models.ForeignKey(related_name='badges', to='badge_site.Issuer'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='issuer',
            name='guid',
            field=models.CharField(help_text=b'This is auto generated and cannot be edited.', unique=True, max_length=24, blank=True),
            preserve_default=True,
        ),
    ]
