# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-29 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(max_length=255, verbose_name='Module')),
                ('path', models.CharField(blank=True, max_length=255, null=True, verbose_name='Path')),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP Address')),
                ('count', models.IntegerField(default=0, verbose_name='Hit count')),
            ],
        ),
    ]
