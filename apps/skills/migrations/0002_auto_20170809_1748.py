# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-09 17:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='icon',
            new_name='image',
        ),
    ]