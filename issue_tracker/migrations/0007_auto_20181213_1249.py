# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-13 12:49
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0006_auto_20181213_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='votes',
            new_name='vote',
        ),
        migrations.AddField(
            model_name='issue',
            name='total_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='issue',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issue',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 13, 12, 49, 22, 419673, tzinfo=utc), null=True),
        ),
    ]
