# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext as _

from resume.models import Work, WorkImage, Education, Interest


class ResumeBaseAdmin(admin.ModelAdmin):
    exclude = (
        'datetime_added',
        'datetime_modified',
        'user',
    )


class WorkImageInline(admin.TabularInline):
    model = WorkImage
    extra = 0
    exclude = (
        'width',
        'height',
        'datetime_added',
        'user',
    )


class WorkAdmin(ResumeBaseAdmin):
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
    )
    readonly_fields = (
        'datetime_added',
        'datetime_modified',
        'user',
    )
    inlines = [
        WorkImageInline,
    ]

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
                'short_description',
                'long_description',
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

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(WorkAdmin, self).save_model(request, obj, form, change)


class EducationAdmin(ResumeBaseAdmin):
    list_display = (
        'title',
        'date_from',
        'date_till',
        'is_published',
    )
    readonly_fields = (
        'datetime_added',
        'datetime_modified',
        'user',
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
                'short_description',
                'long_description',
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


class InterestAdmin(ResumeBaseAdmin):
    list_display = (
        'title',
    )


class WorkImageAdmin(admin.ModelAdmin):
    list_display = (
        'work',
        'is_primary',
        'is_published',
    )
    exclude = (
        'width',
        'height',
        'user',
    )
    readonly_fields = (
        'datetime_added',
        'user',
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
                'datetime_added',
                'user',
            )
        }),
    )


admin.site.register(Work, WorkAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(WorkImage, WorkImageAdmin)

