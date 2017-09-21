# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-21 20:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20170921_2036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='datetime_added',
            new_name='datetime_created',
        ),
        migrations.RenameField(
            model_name='projectimage',
            old_name='datetime_added',
            new_name='datetime_created',
        ),
        migrations.AlterField(
            model_name='project',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_project_created_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AlterField(
            model_name='projectimage',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects_projectimage_created_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
    ]
