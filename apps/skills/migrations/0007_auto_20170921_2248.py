# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-21 22:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0006_skillcategory_is_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skillcategory',
            old_name='frontend_position',
            new_name='position',
        ),
    ]
