# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-23 11:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('feature_requests', '0006_auto_20181223_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 23, 11, 23, 47, 713634, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='featurerequest',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 23, 11, 23, 47, 711791, tzinfo=utc), null=True),
        ),
    ]