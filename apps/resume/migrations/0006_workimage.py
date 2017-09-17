# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-04 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import resume.models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20170903_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, height_field='height', null=True, upload_to=resume.models.work_image_upload_to, verbose_name='Image', width_field='width')),
                ('width', models.IntegerField(null=True, verbose_name='Image width')),
                ('height', models.IntegerField(null=True, verbose_name='Image height')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is published?')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.Work')),
            ],
        ),
    ]