# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-23 13:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('feature_requests', '0013_auto_20190121_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 23, 13, 47, 13, 883957, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='featurerequest',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 23, 13, 47, 13, 881833, tzinfo=utc), null=True),
        ),
    ]
