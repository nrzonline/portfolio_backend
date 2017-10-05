# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext as _
from django import forms
from django.db import models

from profiles.models import Profile
from core.admin.mixins import ModelAdminSetAuditMixin


class ProfileAdmin(ModelAdminSetAuditMixin, admin.ModelAdmin):
    class Meta:
        model = Profile

    readonly_fields = (
        'user',
        'datetime_created',
        'datetime_published',
        'datetime_modified',
        'modified_by',
        'slug',)
    list_display = (
        'user',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'is_published',)
    exclude = (
        'width',
        'height',)
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows': 10, 'cols': 120})}
    }

    fieldsets = (
        (_('User'), {
            'fields': (
                'user',
                'is_published',
            )
        }),
        (_('Personal'), {
            'fields': (
                'photo',
                'first_name',
                'last_name',
                'email',
                'phone_number',
                'date_of_birth',
                'nationality',
                'location',
                'occupation',
            )
        }),
        (_('About'), {
            'fields': (
                'about',
            )
        }),
        (_('Social'), {
            'fields': (
                'website_url',
                'linkedin_url',
                'facebook_url',
                'twitter_url',
                'stackoverflow_url',
                'github_url',
           )
        }),
        (_('Information'), {
            'fields': (
                'modified_by',
                'datetime_modified',
                'datetime_published',
                'slug',
            )
        }),
    )


admin.site.register(Profile, ProfileAdmin)
