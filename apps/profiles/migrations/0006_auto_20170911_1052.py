# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-11 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20170911_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='stackoverflow_url',
            field=models.URLField(blank=True, null=True, verbose_name='Stackoverflow Url'),
        ),
    ]
