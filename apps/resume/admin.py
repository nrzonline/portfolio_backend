# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from resume.models import Work, WorkImage, Education, Interest


class ResumeBaseAdmin(admin.ModelAdmin):
    exclude = (
        'datetime_added',
        'datetime_modified',
    )


class WorkImageInline(admin.TabularInline):
    model = WorkImage
    extra = 0
    exclude = (
        'width',
        'height',
        'datetime_added',
    )


class WorkAdmin(ResumeBaseAdmin):
    exclude = (
        'width',
        'height',
    )
    list_display = (
        'title',
        'date_from',
        'date_till',
        'is_published',
    )
    inlines = [
        WorkImageInline,
    ]


class EducationAdmin(ResumeBaseAdmin):
    list_display = (
        'title',
        'date_from',
        'date_till',
        'is_published',
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
    exclude = ('width', 'height', )


admin.site.register(Work, WorkAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(WorkImage, WorkImageAdmin)

