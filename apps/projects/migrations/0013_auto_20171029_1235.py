# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-29 12:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20170927_0724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectattachment',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='projectattachment',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='projectattachment',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectattachment',
            name='published_by',
        ),
        migrations.RemoveField(
            model_name='projectimage',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='projectimage',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='projectimage',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectimage',
            name='published_by',
        ),
        migrations.RemoveField(
            model_name='projectlink',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='projectlink',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='projectlink',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectlink',
            name='published_by',
        ),
        migrations.DeleteModel(
            name='ProjectAttachment',
        ),
        migrations.DeleteModel(
            name='ProjectImage',
        ),
        migrations.DeleteModel(
            name='ProjectLink',
        ),
    ]
