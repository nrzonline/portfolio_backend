# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from about.models import About


class AboutAdmin(admin.ModelAdmin):
    class Meta:
        model = About

    exclude = ()
    list_display = ('first_name', 'last_name', 'email', 'phone_number',)


admin.site.register(About, AboutAdmin)
