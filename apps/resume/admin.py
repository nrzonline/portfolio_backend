# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext as _

from resume.models import Work, WorkImage, Education, Interest


class WorkImageInline(admin.TabularInline):
    model = WorkImage
    extra = 0
    fields = (
        'title',
        'description',
        'image',
        'is_primary',
        'is_published',
    )


class WorkAdmin(admin.ModelAdmin):
    exclude = (
        'width',
        'height',
    )
    list_display = (
        'title',
        'organization',
        'organization_image',
        'date_from',
        'date_till',
        'is_published',
    )
    readonly_fields = (
        'published_by',
        'datetime_published',
        'created_by',
        'datetime_created',
        'modified_by',
        'datetime_modified',
    )

    fieldsets = (
        (_('Publish'), {
            'fields': (
                'is_published',
            )
        }),
        (_('Details'), {
            'fields': (
                'date_from',
                'date_till',
                'organization',
                'organization_image',
            )
        }),
        (_('Content'), {
            'fields': (
                'title',
                'description',
                'content',
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

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.request = request
        return super(WorkAdmin, self).save_model(request, obj, form, change)


class EducationAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date_from',
        'date_till',
        'datetime_created',
        'datetime_modified',
        'is_published',
    )
    readonly_fields = (
        'published_by',
        'datetime_published',
        'created_by',
        'datetime_created',
        'modified_by',
        'datetime_modified',
    )

    fieldsets = (
        (_('Publish'), {
            'fields': (
                'is_published',
            )
        }),
        (_('Details'), {
            'fields': (
                'date_from',
                'date_till',
            )
        }),
        (_('Content'), {
            'fields': (
                'title',
                'description',
                'content',
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


class InterestAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
        'datetime_created',
        'datetime_modified',
        'is_published',
    )
    readonly_fields = (
        'published_by',
        'datetime_published',
        'created_by',
        'datetime_created',
        'modified_by',
        'datetime_modified',
    )

    fieldsets = (
        (_('Publish'), {
            'fields': (
                'is_published',
            )
        }),
        (_('Content'), {
            'fields': (
                'title',
                'description',
                'content',
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


class WorkImageAdmin(admin.ModelAdmin):
    list_display = (
        'work',
        'image',
        'is_primary',
        'datetime_created',
        'datetime_modified',
        'is_published',
    )
    exclude = (
        'width',
        'height',
        'created_by',
    )
    readonly_fields = (
        'published_by',
        'datetime_published',
        'created_by',
        'datetime_created',
        'modified_by',
        'datetime_modified',
    )

    fieldsets = (
        (_('Publish'), {
            'fields': (
                'is_published',
            )
        }),
        (_('Content'), {
            'fields': (
                'work',
                'image',
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


admin.site.register(Work, WorkAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(WorkImage, WorkImageAdmin)

