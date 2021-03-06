# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext as _

from skills.models import Skill, SkillCategory
from core.admin.mixins import ModelAdminSetAuditMixin


class SkillAdmin(ModelAdminSetAuditMixin):
    exclude = (
        'width',
        'height',
        'datetime_created',
        'datetime_modified',
        'slug',
    )
    list_display = (
        'title',
        'category',
        'level_max',
        'level',
        'image',
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
        'slug',
    )

    fieldsets = (
        (_('Publish'), {
            'fields': (
                'is_published',
                'category',
            )
        }),
        (_('Details'), {
            'fields': (
                'title',
                'description',
                'content',
                'image',
                'level',
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


class SkillCategoryAdmin(ModelAdminSetAuditMixin):
    exclude = (
        'slug',
    )
    list_display = (
        'title',
        'position',
        'datetime_created',
        'datetime_modified',
        'is_published',
    )

    fieldsets = (
        (_('Publish'), {
            'fields': (
                'is_published',
            )
        }),
        (_('Category'), {
            'fields': (
                'title',
                'description',
                'position',
            )
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.request = request
        return super(SkillCategoryAdmin, self).save_model(request, obj, form, change)

admin.site.register(SkillCategory, SkillCategoryAdmin)
admin.site.register(Skill, SkillAdmin)
