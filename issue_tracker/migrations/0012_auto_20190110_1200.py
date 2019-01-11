# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-10 12:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0011_auto_20190109_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 10, 12, 0, 33, 734254, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 10, 12, 0, 33, 731669, tzinfo=utc), null=True),
        ),
    ]