# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-30 09:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='rating',
            new_name='vote',
        ),
    ]