# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from statistics.models import RequestCount


class RequestCountAdmin(admin.ModelAdmin):
    class Meta:
        model = RequestCount

    exclude = ()
    list_display = ('module', 'path', 'ip_address', 'count', 'datetime',)

admin.site.register(RequestCount, RequestCountAdmin)

