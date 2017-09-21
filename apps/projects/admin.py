# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext as _

from projects.models import (
    Project, ProjectImage, ProjectAttachment, ProjectLink)
from utils.admin.options import ModelAdminSaveUserOnCreate


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    fk_name = 'project'
    extra = 0
    exclude = (
        'width',
        'height',
        'datetime_added',
        'datetime_modified',
        'slug',
        'user',
    )


class ProjectAttachmentInline(admin.TabularInline):
    model = ProjectAttachment
    fk_name = 'project'
    extra = 0
    exclude = (
        'datetime_added',
        'datetime_modified',
        'slug',
        'user',
    )


class ProjectLinkInline(admin.TabularInline):
    model = ProjectLink
    fk_name = 'project'
    extra = 0
    exclude = (
        'datetime_added',
        'datetime_modified',
        'user',
    )


class ProjectAdmin(ModelAdminSaveUserOnCreate, admin.ModelAdmin):
    exclude = (
        'datetime_added',
        'datetime_modified',
        'slug',
    )
    list_display = (
        'title',
        'is_published',
        'datetime_added',
        'datetime_modified',
    )
    readonly_fields = (
        'datetime_added',
        'datetime_modified',
        'slug',
        'user',
    )
    filter_horizontal = (
        'skills',
    )
    inlines = [
        ProjectImageInline,
        ProjectAttachmentInline,
        ProjectLinkInline,
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
                'short_description',
                'full_description',
                'skills',
            )
        }),
        (_('Information'), {
            'fields': (
                'datetime_added',
                'datetime_modified',
                'slug',
                'user',
            )
        }),
    )


class ProjectImageAdmin(ModelAdminSaveUserOnCreate, admin.ModelAdmin):
    exclude = (
        'width',
        'height',
        'datetime_added',
        'datetime_modified',
        'slug',
    )
    list_display = (
        'title',
        'project',
        'image',
        'is_primary',
        'is_published',
    )
    readonly_fields = (
        'datetime_added',
        'datetime_modified',
        'slug',
        'user',
    )

    fieldsets = (
        (_('Publish'), {
            'fields': (
                'is_published',
            )
        }),
        (_('Image details'), {
            'fields': (
                'project',
                'title',
                'image',
                'description',
                'is_primary',
            )
        }),
        (_('Information'), {
            'fields': (
                'datetime_added',
                'datetime_modified',
                'slug',
                'user',
            )
        }),
    )


class ProjectAttachmentAdmin(ModelAdminSaveUserOnCreate, admin.ModelAdmin):
    exclude = (
        'datetime_added',
        'datetime_modified',
        'user',
        'slug',
    )
    list_display = (
        'title',
        'project',
        'file',
        'is_published',
        'datetime_added',
        'datetime_modified',
    )
    readonly_fields = (
        'datetime_added',
        'datetime_modified',
        'slug',
        'user',
    )

    fieldsets = (
        (_('Attachment details'), {
            'fields': (
                'project',
                'title',
                'file',
                'description',
            )
        }),
        (_('Information'), {
            'fields': (
                'datetime_added',
                'datetime_modified',
                'slug',
                'user',
            )
        }),
    )


class ProjectLinkAdmin(ModelAdminSaveUserOnCreate, admin.ModelAdmin):
    exclude = (
        'datetime_added',
        'datetime_modified',
        'user',
    )
    list_display = (
        'title',
        'project',
        'url',
        'is_published',
        'datetime_added',
        'datetime_modified',
    )
    readonly_fields = (
        'datetime_added',
        'datetime_modified',
        'user',
    )

    fieldsets = (
        (_('Attachment details'), {
            'fields': (
                'project',
                'title',
                'file',
                'description',
            )
        }),
        (_('Information'), {
            'fields': (
                'datetime_added',
                'datetime_modified',
                'user',
            )
        }),
    )

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
admin.site.register(ProjectAttachment, ProjectAttachmentAdmin)
admin.site.register(ProjectLink, ProjectLinkAdmin)
