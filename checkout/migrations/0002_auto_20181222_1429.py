# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-22 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singlepayment',
            name='postcode',
            field=models.CharField(max_length=15),
        ),
    ]