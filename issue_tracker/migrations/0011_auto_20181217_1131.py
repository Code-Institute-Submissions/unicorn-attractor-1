# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-17 11:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0010_auto_20181213_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 17, 11, 31, 11, 469248, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 17, 11, 31, 11, 466999, tzinfo=utc), null=True),
        ),
    ]
