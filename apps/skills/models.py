# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from core.services import unique_filename
from core.models.mixins import ContentMixin, AuditMixin, PublishMixin, SlugifyMixin


def skill_image_upload_location(instance, filename):
    filename = unique_filename(filename)
    return 'uploads/skills/images/%s' % filename


class Skill(ContentMixin, AuditMixin, PublishMixin, SlugifyMixin):
    category = models.ForeignKey('skills.SkillCategory')
    level_max = models.IntegerField(_("Level caps"), default=5)
    level = models.IntegerField(_("Current skill level"))
    image = models.ImageField(_("Image"), upload_to=skill_image_upload_location,
                              width_field='width', height_field='height',
                              null=True, blank=True)
    width = models.IntegerField(_("Image width"), null=True, blank=True)
    height = models.IntegerField(_("Image height"), null=True, blank=True)

    def __str__(self):
        return self.title


class SkillCategory(AuditMixin, PublishMixin, SlugifyMixin):
    class Meta:
        verbose_name_plural = _("Skill categories")

    title = models.CharField(_("Category title"), max_length=50)
    description = models.CharField(_("Description"), max_length=500)
    position = models.IntegerField(_("Position on frontend"))

    @property
    def skills(self):
        return Skill.objects.filter(category=self.id)

    def __str__(self):
        return self.title
