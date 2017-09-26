# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext as _

from projects.models import Project, ProjectImage, ProjectAttachment, ProjectLink
from core.admin.mixins import ModelAdminSetAuditMixin


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    fk_name = 'project'
    extra = 0
    fields = (
        'title',
        'description',
        'image',
        'is_primary',
        'is_published',
    )


class ProjectAttachmentInline(admin.TabularInline):
    model = ProjectAttachment
    fk_name = 'project'
    extra = 0
    fields = (
        'title',
        'description',
        'file',
        'is_published',
    )


class ProjectLinkInline(admin.TabularInline):
    model = ProjectLink
    fk_name = 'project'
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


class ProjectImageAdmin(ModelAdminSetAuditMixin, admin.ModelAdmin):
    exclude = (
        'width',
        'height',
        'datetime_created',
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
        'created_by',
        'datetime_created',
        'modified_by',
        'datetime_modified',
        'datetime_published',
        'slug',
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
                'created_by',
                'datetime_created',
                'modified_by',
                'datetime_modified',
                'datetime_published',
                'slug',
            )
        }),
    )


class ProjectAttachmentAdmin(ModelAdminSetAuditMixin, admin.ModelAdmin):
    exclude = (
        'datetime_created',
        'datetime_modified',
        'created_by',
        'slug',
    )
    list_display = (
        'project',
        'title',
        'file',
        'datetime_created',
        'datetime_modified',
        'is_published',
    )
    readonly_fields = (
        'created_by',
        'datetime_created',
        'modified_by',
        'datetime_modified',
        'datetime_published',
        'slug',
    )

    fieldsets = (
        (_('Publish'), {
            'fields': (
                'is_published',
            )
        }),
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
                'created_by',
                'datetime_created',
                'modified_by',
                'datetime_modified',
                'datetime_published',
                'slug',
            )
        }),
    )


class ProjectLinkAdmin(ModelAdminSetAuditMixin, admin.ModelAdmin):
    exclude = (
        'datetime_created',
        'datetime_modified',
        'created_by',
    )
    list_display = (
        'project',
        'title',
        'url',
        'description',
        'datetime_created',
        'datetime_modified',
        'is_published',
    )
    readonly_fields = (
        'created_by',
        'datetime_created',
        'modified_by',
        'datetime_modified',
        'datetime_published',
    )

    fieldsets = (
        (_('Publish'), {
            'fields': (
                'is_published',
            )
        }),
        (_('Attachment details'), {
            'fields': (
                'project',
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

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
admin.site.register(ProjectAttachment, ProjectAttachmentAdmin)
admin.site.register(ProjectLink, ProjectLinkAdmin)
