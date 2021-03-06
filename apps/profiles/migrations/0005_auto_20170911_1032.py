# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-11 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_occupation'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='github_url',
            field=models.URLField(blank=True, null=True, verbose_name='GitHub Url'),
        ),
        migrations.AddField(
            model_name='profile',
            name='stackoverflow_url',
            field=models.URLField(blank=True, null=True, verbose_name='LinkedIn Url'),
        ),
    ]
