# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-30 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='title',
            field=models.CharField(max_length=50, verbose_name='File name'),
        ),
    ]
