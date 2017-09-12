# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = Profile

    exclude = ()
    list_display = ('account', 'first_name', 'last_name', 'email', 'phone_number',)


admin.site.register(Profile, ProfileAdmin)
