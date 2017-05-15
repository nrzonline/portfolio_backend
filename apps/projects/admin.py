# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from projects.models import (
    Project, ProjectImage, ProjectAttachment, ProjectLink)


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
    )


class ProjectAttachmentInline(admin.TabularInline):
    model = ProjectAttachment
    fk_name = 'project'
    extra = 0
    exclude = (
        'width',
        'height',
        'datetime_added',
        'datetime_modified',
        'slug',
    )


class ProjectLinkInline(admin.TabularInline):
    model = ProjectLink
    fk_name = 'project'
    extra = 0
    exclude = (
        'datetime_added',
        'datetime_modified',
        'slug',
    )


class ProjectAdmin(admin.ModelAdmin):
    class Meta:
        model = Project

    exclude = (
        'datetime_added',
        'datetime_modified',
        'slug',)
    list_display = (
        'title',
        'is_published',
        'datetime_added',
        'datetime_modified',)
    inlines = [
        ProjectImageInline,
        ProjectAttachmentInline,
        ProjectLinkInline,
    ]


class ProjectImageAdmin(admin.ModelAdmin):
    class Meta:
        model = ProjectImage

    exclude = (
        'width',
        'height',
        'datetime_added',
        'datetime_modified',
        'slug',)
    list_display = (
        'title',
        'project',
        'image',
        'is_primary',
        'is_published',
        'datetime_added',
        'datetime_modified',)


class ProjectAttachmentAdmin(admin.ModelAdmin):
    class Meta:
        model = ProjectAttachment

    exclude = (
        'datetime_added',
        'datetime_modified',
        'slug',)
    list_display = (
        'title',
        'project',
        'file',
        'is_published',
        'datetime_added',
        'datetime_modified',)


class ProjectLinkAdmin(admin.ModelAdmin):
    class Meta:
        model = ProjectLink

    exclude = (
        'datetime_added',
        'datetime_modified',)
    list_display = (
        'title',
        'project',
        'url',
        'is_published',
        'datetime_added',
        'datetime_modified',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage, ProjectImageAdmin)
admin.site.register(ProjectAttachment, ProjectAttachmentAdmin)
admin.site.register(ProjectLink, ProjectLinkAdmin)
