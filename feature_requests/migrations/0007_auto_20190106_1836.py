# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-06 18:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('feature_requests', '0006_auto_20190106_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 6, 18, 36, 56, 376986, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='featurerequest',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 6, 18, 36, 56, 375063, tzinfo=utc), null=True),
        ),
    ]
