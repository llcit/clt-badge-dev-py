# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', models.CharField(help_text=b'This is auto generated.', unique=True, max_length=10)),
                ('email', models.CharField(help_text=b'Email for the recipient (use the email the user intends to use with their Mozilla Backpack account).', max_length=1024)),
                ('firstname', models.CharField(max_length=1024)),
                ('lastname', models.CharField(max_length=1024)),
                ('issuedOn', models.DateTimeField(auto_now_add=True)),
                ('evidence', models.URLField(help_text=b'URL that points a resource that provides evidence for this award.', max_length=1024)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('claimCode', models.CharField(help_text=b'This is auto generated. Send this to recipient so they may claim their badge.', max_length=10, blank=True)),
                ('salt', models.CharField(help_text=b'This is auto generated.', max_length=10, blank=True)),
                ('jsonfile', models.URLField(help_text=b'This is auto generated but is fully qualified url for the award assertion.', max_length=1024, blank=True)),
                ('expires', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', models.CharField(unique=True, max_length=10)),
                ('name', models.CharField(max_length=1024)),
                ('image', models.URLField()),
                ('description', models.CharField(max_length=128)),
                ('criteria', models.URLField()),
                ('created', models.DateField(auto_now=True)),
                ('jsonfile', models.URLField(max_length=1024, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issuer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guid', models.CharField(help_text=b'This is auto generated.', unique=True, max_length=10)),
                ('name', models.CharField(max_length=128)),
                ('initials', models.CharField(max_length=32)),
                ('url', models.CharField(max_length=128)),
                ('doc_path', models.CharField(max_length=512)),
                ('desc', models.CharField(max_length=512)),
                ('image', models.CharField(max_length=128)),
                ('contact', models.CharField(max_length=128)),
                ('jsonfile', models.URLField(max_length=1024, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='badge',
            name='issuer',
            field=models.ForeignKey(to='badge_site.Issuer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='award',
            name='badge',
            field=models.ForeignKey(to='badge_site.Badge'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='award',
            name='creator',
            field=models.ForeignKey(related_name='award_creator', blank=True, to=settings.AUTH_USER_MODEL, help_text=b'Specify yourself.', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='award',
            unique_together=set([('email', 'badge')]),
        ),
    ]
