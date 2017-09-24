# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext as _
from django import forms
from django.db import models

from profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = Profile

    readonly_fields = ('account',)
    list_display = ('account', 'first_name', 'last_name', 'email', 'phone_number', 'is_published',)
    exclude = ('width', 'height',)
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows': 10, 'cols': 120})}
    }

    fieldsets = (
        (_('Account'), {
            'fields': (
                'account',
            )
        }),
        (_('Publish'), {
            'fields': (
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
        })
    )


admin.site.register(Profile, ProfileAdmin)
