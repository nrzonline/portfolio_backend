# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-17 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20170911_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Profile published?'),
        ),
    ]
