# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-09 20:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0010_auto_20190109_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 9, 20, 46, 50, 745085, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 9, 20, 46, 50, 743035, tzinfo=utc), null=True),
        ),
    ]