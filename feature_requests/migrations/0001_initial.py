# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-18 19:00
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('content', models.TextField(max_length=100, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('published_date', models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 18, 19, 0, 40, 533276, tzinfo=utc), null=True)),
                ('tag', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeatureRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('content', models.TextField(max_length=2000)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('published_date', models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 18, 19, 0, 40, 531300, tzinfo=utc), null=True)),
                ('total_votes', models.IntegerField(default=0)),
                ('tag', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('done', models.BooleanField(default=False)),
                ('comment_number', models.IntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vote', models.ManyToManyField(blank=True, related_name='feature_votes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='feature_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feature_requests.FeatureRequest'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_logged_in',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_logged_in', to=settings.AUTH_USER_MODEL),
        ),
    ]
