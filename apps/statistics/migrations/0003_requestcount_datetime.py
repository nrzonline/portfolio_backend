# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-01 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0002_auto_20170830_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestcount',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
