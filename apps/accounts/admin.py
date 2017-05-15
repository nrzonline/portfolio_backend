# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import Permission


class PermissionAdmin(admin.ModelAdmin):
    class Meta:
        model = Permission

    exclude = ()
    list_display = (
        'content_type',
        'codename',
        'name',)

admin.site.register(Permission, PermissionAdmin)
