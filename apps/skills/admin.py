# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from skills.models import Skill, SkillCategory


class SkillAdmin(admin.ModelAdmin):
    class Meta:
        model = Skill

    exclude = (
        'width',
        'height',
        'datetime_added',
        'datetime_modified',
        'slug',)
    list_display = (
        'title',
        'category',
        'level_max',
        'level',
        'is_published',
        'image',
        'datetime_added',
        'datetime_modified',)


class SkillCategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = SkillCategory

    exclude = ('slug',)
    list_display = ('title', 'frontend_position', 'is_published',)

admin.site.register(SkillCategory, SkillCategoryAdmin)
admin.site.register(Skill, SkillAdmin)
