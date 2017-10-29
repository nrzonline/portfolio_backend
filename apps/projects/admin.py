# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.translation import ugettext as _

from projects.models import Project
from multimedia.models import Image, File, Link
from core.admin.mixins import ModelAdminSetAuditMixin


class ImageInline(GenericTabularInline):
    model = Image
    extra = 0
    fields = (
        'title',
        'description',
        'image',
        'is_primary',
        'is_published',
    )


class FileInline(GenericTabularInline):
    model = File
    extra = 0
    fields = (
        'title',
        'description',
        'file',
        'is_published',
    )


class LinkInline(GenericTabularInline):
    model = Link
    extra = 0
    fields = (
        'title',
        'description',
        'url',
        'is_published',
    )


class ProjectAdmin(ModelAdminSetAuditMixin, admin.ModelAdmin):
    exclude = (
        'datetime_created',
        'datetime_modified',
        'slug',
    )
    list_display = (
        'title',
        'datetime_created',
        'datetime_modified',
        'created_by',
        'is_published',
    )
    readonly_fields = (
        'published_by',
        'datetime_published',
        'created_by',
        'datetime_created',
        'modified_by',
        'datetime_modified',
        'slug',
    )
    filter_horizontal = (
        'skills',
    )
    inlines = [
        ImageInline,
        FileInline,
        LinkInline,
    ]

    fieldsets = (
        (_('Publish'), {
            'fields': (
                'is_published',
            )
        }),
        (_('Project details'), {
            'fields': (
                'title',
                'description',
                'content',
                'skills',
            )
        }),
        (_('Information'), {
            'fields': (
                'created_by',
                'datetime_created',
                'modified_by',
                'datetime_modified',
                'datetime_published',
                'slug',
            )
        }),
    )

admin.site.register(Project, ProjectAdmin)
