# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-26 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0004_auto_20170901_0915'),
        ('projects', '0010_auto_20170921_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='votes',
            field=models.ManyToManyField(blank=True, to='votes.Vote'),
        ),
    ]
