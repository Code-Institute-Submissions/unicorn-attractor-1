# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-03 17:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('feature_requests', '0010_auto_20190103_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 3, 17, 14, 36, 281006, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='featurerequest',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 3, 17, 14, 36, 279163, tzinfo=utc), null=True),
        ),
    ]
