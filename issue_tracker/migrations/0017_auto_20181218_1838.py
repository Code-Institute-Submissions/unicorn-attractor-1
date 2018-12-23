# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-18 18:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0016_auto_20181218_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 18, 18, 38, 7, 848303, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 18, 18, 38, 7, 846031, tzinfo=utc), null=True),
        ),
    ]