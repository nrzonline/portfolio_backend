# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-21 23:07
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('skills', '0007_auto_20170921_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='datetime_added',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='full_description',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='short_description',
        ),
        migrations.AddField(
            model_name='skill',
            name='content',
            field=models.TextField(default=1, max_length=5000, verbose_name='Content body'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='skills_skill_created_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 9, 21, 23, 6, 54, 902837), verbose_name='Created on'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='datetime_published',
            field=models.DateTimeField(blank=True, null=True, verbose_name='First published on'),
        ),
        migrations.AddField(
            model_name='skill',
            name='description',
            field=models.TextField(default='description', max_length=1500, verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skills_skill_modified_related', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AddField(
            model_name='skill',
            name='published_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skills_skill_publish_related', to=settings.AUTH_USER_MODEL, verbose_name='First published by'),
        ),
        migrations.AddField(
            model_name='skillcategory',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='skills_skillcategory_created_related', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skillcategory',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created on'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skillcategory',
            name='datetime_modified',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Modified on'),
        ),
        migrations.AddField(
            model_name='skillcategory',
            name='datetime_published',
            field=models.DateTimeField(blank=True, null=True, verbose_name='First published on'),
        ),
        migrations.AddField(
            model_name='skillcategory',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skills_skillcategory_modified_related', to=settings.AUTH_USER_MODEL, verbose_name='Modified by'),
        ),
        migrations.AddField(
            model_name='skillcategory',
            name='published_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skills_skillcategory_publish_related', to=settings.AUTH_USER_MODEL, verbose_name='First published by'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Is published?'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Title'),
        ),
    ]
