# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-13 12:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0007_auto_20181213_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 13, 12, 49, 33, 865129, tzinfo=utc), null=True),
        ),
    ]