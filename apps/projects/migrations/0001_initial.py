# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 16:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multimedia.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Project title')),
                ('short_description', models.CharField(max_length=1500, verbose_name='Short description')),
                ('full_description', models.CharField(max_length=5000, verbose_name='Full description')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Project URL')),
                ('is_published', models.BooleanField(verbose_name='Is published?')),
                ('datetime_added', models.DateTimeField(auto_now_add=True, verbose_name='Added on')),
                ('datetime_modified', models.DateTimeField(blank=True, null=True, verbose_name='Updated on')),
                ('slug', models.SlugField()),
                ('skills', models.ManyToManyField(to='skills.Skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Attachment name')),
                ('description', models.CharField(max_length=1500, verbose_name='Description')),
                ('file', models.FileField(upload_to=multimedia.models.upload_image_location, verbose_name='Attachment')),
                ('is_published', models.BooleanField(verbose_name='Is published?')),
                ('datetime_added', models.DateTimeField(auto_now_add=True, verbose_name='Added on')),
                ('datetime_modified', models.DateTimeField(blank=True, null=True, verbose_name='Updated on')),
                ('slug', models.SlugField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Submitted by')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Image name')),
                ('description', models.CharField(max_length=1500, verbose_name='Description')),
                ('image', models.ImageField(height_field='height', upload_to=multimedia.models.upload_image_location, verbose_name='Screenshot', width_field='width')),
                ('width', models.IntegerField(verbose_name='Image width')),
                ('height', models.IntegerField(verbose_name='Image height')),
                ('is_primary', models.BooleanField(default=False, verbose_name='Primary Image?')),
                ('is_published', models.BooleanField(verbose_name='Is published?')),
                ('datetime_added', models.DateTimeField(auto_now_add=True, verbose_name='Added on')),
                ('datetime_modified', models.DateTimeField(blank=True, null=True, verbose_name='Updated on')),
                ('slug', models.SlugField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Submitted by')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Link name')),
                ('description', models.CharField(max_length=1500)),
                ('url', models.URLField(max_length=255, verbose_name='Url')),
                ('is_published', models.BooleanField(verbose_name='Is published?')),
                ('datetime_added', models.DateTimeField(auto_now_add=True, verbose_name='Added on')),
                ('datetime_modified', models.DateTimeField(blank=True, null=True, verbose_name='Updated on')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Added by')),
            ],
        ),
    ]
