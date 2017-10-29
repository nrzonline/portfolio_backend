# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.contenttypes.models import ContentType

from core.models.mixins import CompleteArticleMixin
from multimedia.models import Image, File, Link


class Project(CompleteArticleMixin, models.Model):
    url = models.URLField(_("Project URL"), null=True, blank=True)
    skills = models.ManyToManyField('skills.Skill', verbose_name=_("Related skills"))

    @property
    def primary_image(self):
        primary_image = Image.objects.filter(
            content_type=ContentType.objects.get_for_model(self),
            object_id=self.id,
            is_primary=True)

        if primary_image:
            return primary_image.last()
        return None

    @property
    def published_images(self):
        return Image.objects.filter(
            content_type=ContentType.objects.get_for_model(self),
            object_id=self.id,
            is_published=True
        ).order_by('-is_primary')

    @property
    def published_files(self):
        return File.objects.filter(
            content_type=ContentType.objects.get_for_model(self),
            object_id=self.id,
            is_published=True)

    @property
    def published_links(self):
        return Link.objects.filter(
            content_type=ContentType.objects.get_for_model(self),
            object_id=self.id,
            is_published=True)

    def __str__(self):
        return self.title
