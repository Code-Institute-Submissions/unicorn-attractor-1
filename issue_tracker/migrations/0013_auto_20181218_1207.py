# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-18 12:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0012_auto_20181218_1155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='comments',
            new_name='comment_number',
        ),
        migrations.AlterField(
            model_name='comment',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 18, 12, 7, 3, 20194, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='issue',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 18, 12, 7, 3, 17770, tzinfo=utc), null=True),
        ),
    ]