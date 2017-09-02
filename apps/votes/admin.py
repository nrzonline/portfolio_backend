# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from votes.models import Vote


class VoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Vote

    exclude = ()
    list_display = ('vote', 'content_type', 'object_id', 'ip_address', 'datetime',)

admin.site.register(Vote, VoteAdmin)

