# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-10 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20190106_1305'),
        ('checkout', '0002_singlepayment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='singlepaymentlineitem',
            name='user_paid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.UserProfile'),
        ),
    ]
