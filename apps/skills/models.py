# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext as _

from utils.services import unique_filename


def skill_icon_upload_location(instance, filename):
    filename = unique_filename(filename)
    return 'uploads/skills/icons/%s' % filename


class Skill(models.Model):
    title = models.CharField(
        _("Skill title"),
        max_length=50)
    short_description = models.CharField(
        _("Short description"),
        max_length=500)
    full_description = models.CharField(
        _("Full description"),
        max_length=5000)
    category = models.ForeignKey(
        'skills.SkillCategory')
    level_max = models.IntegerField(
        _("Level caps"),
        default=5)
    level = models.IntegerField(
        _("Current skill level"))
    is_published = models.BooleanField(
        _("Is published?"))
    icon = models.ImageField(
        _("Icon"),
        width_field='width',
        height_field='height',
        upload_to=skill_icon_upload_location,
        null=True, blank=True)
    width = models.IntegerField(
        _("Icon width"),
        null=True, blank=True)
    height = models.IntegerField(
        _("Icon height"),
        null=True, blank=True)
    datetime_added = models.DateTimeField(
        auto_now_add=True)
    datetime_modified = models.DateTimeField(
        _("Modified on"),
        null=True, blank=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.update_datetime_modified()
        return super(Skill, self).save(*args, **kwargs)

    def update_datetime_modified(self):
        if self.id:
            self.datetime_modified = datetime.now()

    def __unicode__(self):
        return self.title


class SkillCategory(models.Model):
    class Meta:
        verbose_name_plural = _("Skill categories")

    title = models.CharField(
        _("Category title"),
        max_length=50)
    description = models.CharField(
        _("Description"),
        max_length=500)
    frontend_position = models.IntegerField(
        _("Position on frontend"))
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(SkillCategory, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
