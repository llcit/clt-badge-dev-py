# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-27 21:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badge_site', '0014_auto_20150428_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='claimCode',
            field=models.CharField(blank=True, help_text='This is auto generated. Send this to recipient so they may claim their badge.', max_length=10),
        ),
        migrations.AlterField(
            model_name='award',
            name='creator',
            field=models.ForeignKey(blank=True, help_text='Specify yourself.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='award_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='award',
            name='email',
            field=models.CharField(help_text='Email for the recipient (use the email the user intends to use with their Mozilla Backpack account).', max_length=1024),
        ),
        migrations.AlterField(
            model_name='award',
            name='evidence',
            field=models.URLField(help_text='URL that points to a resource that provides evidence for this award.', max_length=1024),
        ),
        migrations.AlterField(
            model_name='award',
            name='guid',
            field=models.CharField(help_text='This is auto generated.', max_length=24, unique=True),
        ),
        migrations.AlterField(
            model_name='award',
            name='jsonfile',
            field=models.URLField(blank=True, help_text='This is auto generated but is fully qualified url for the award assertion.', max_length=1024),
        ),
        migrations.AlterField(
            model_name='award',
            name='salt',
            field=models.CharField(blank=True, help_text='This is auto generated.', max_length=10),
        ),
        migrations.AlterField(
            model_name='badge',
            name='notify_email_message',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='badge',
            name='notify_email_subject',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='issuer',
            name='guid',
            field=models.CharField(blank=True, help_text='This is auto generated and cannot be edited.', max_length=24, unique=True),
        ),
        migrations.AlterField(
            model_name='revocation',
            name='award',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='badge_site.Award'),
        ),
    ]