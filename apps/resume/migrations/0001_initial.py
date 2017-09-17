# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-02 23:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('short_description', models.TextField(max_length=2000, verbose_name='Short description')),
                ('long_description', models.TextField(max_length=5000, verbose_name='Long description')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is published?')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('resumebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resume.ResumeBase')),
                ('date_from', models.DateField(blank=True, null=True, verbose_name='From')),
                ('date_till', models.DateField(blank=True, null=True, verbose_name='Till')),
                ('year', models.DateField(blank=True, null=True, verbose_name='Year')),
                ('duration', models.IntegerField(blank=True, null=True, verbose_name='Duration')),
            ],
            bases=('resume.resumebase',),
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('resumebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resume.ResumeBase')),
            ],
            bases=('resume.resumebase',),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('resumebase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='resume.ResumeBase')),
                ('organization', models.CharField(max_length=255, verbose_name='Organization')),
                ('date_from', models.DateField(verbose_name='From')),
                ('date_till', models.DateField(verbose_name='Till')),
            ],
            bases=('resume.resumebase',),
        ),
    ]