# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from multimedia.models import Image, File, Link
from core.admin.mixins import ModelAdminSetAuditMixin, ContentObjectFieldMixin


class ImageAdmin(ModelAdminSetAuditMixin, ContentObjectFieldMixin, admin.ModelAdmin):
    exclude = (
        'width',
        'height',
        'datetime_created',
        'datetime_modified',
    )
    list_display = (
        'title',
        'related_content_object',
        'image',
        'is_primary',
        'is_published',
    )
    readonly_fields = (
        'content_type',
        'object_id',
        'created_by',
        'datetime_created',
        'modified_by',
        'datetime_modified',
        'datetime_published',
    )

    fieldsets = (
        (_('Parent object'), {
            'fields': (
                'content_type',
                'object_id',
            ),
        }),
        (_('Publish'), {
            'fields': (
                'is_published',
            )
        }),
        (_('Image details'), {
            'fields': (
                'title',
                'image',
                'description',
                'is_primary',
            )
        }),
        (_('Information'), {
            'fields': (
                'created_by',
                'datetime_created',
                'modified_by',
                'datetime_modified',
                'datetime_published',
            )
        }),
    )


class FileAdmin(ModelAdminSetAuditMixin, ContentObjectFieldMixin, admin.ModelAdmin):
    exclude = (
        'datetime_created',
        'datetime_modified',
        'created_by',
    )
    list_display = (
        'title',
        'related_content_object',
        'file',
        'datetime_created',
        'datetime_modified',
        'is_published',
    )
    readonly_fields = (
        'content_type',
        'object_id',
        'created_by',
        'datetime_created',
        'modified_by',
        'datetime_modified',
        'datetime_published',
    )

    fieldsets = (
        (_('Parent object'), {
            'fields': (
                'content_type',
                'object_id',
            ),
        }),
        (_('Publish'), {
            'fields': (
                'is_published',
            )
        }),
        (_('Attachment details'), {
            'fields': (
                'title',
                'file',
                'description',
            )
        }),
        (_('Information'), {
            'fields': (
                'created_by',
                'datetime_created',
                'modified_by',
                'datetime_modified',
                'datetime_published',
            )
        }),
    )


class LinkAdmin(ModelAdminSetAuditMixin, ContentObjectFieldMixin, admin.ModelAdmin):
    exclude = (
        'datetime_created',
        'datetime_modified',
        'created_by',
    )
    list_display = (
        'title',
        'related_content_object',
        'url',
        'description',
        'datetime_created',
        'datetime_modified',
        'is_published',
    )
    readonly_fields = (
        'content_type',
        'object_id',
        'created_by',
        'datetime_created',
        'modified_by',
        'datetime_modified',
        'datetime_published',
    )

    fieldsets = (
        (_('Parent object'), {
            'fields': (
                'content_type',
                'object_id',
            ),
        }),
        (_('Publish'), {
            'fields': (
                'is_published',
            )
        }),
        (_('Attachment details'), {
            'fields': (
                'title',
                'description',
                'url',
            )
        }),
        (_('Information'), {
            'fields': (
                'created_by',
                'datetime_created',
                'modified_by',
                'datetime_modified',
                'datetime_published',
            )
        }),
    )

admin.site.register(Image, ImageAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Link, LinkAdmin)
