# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from utils.services import unique_filename


class ResumeBase(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    short_description = models.TextField(_("Short description"), max_length=2000)
    long_description = models.TextField(_("Long description"), max_length=5000)
    datetime_added = models.DateTimeField(_("Added on"), auto_now_add=True)
    datetime_modified = models.DateTimeField(_("Modified on"), null=True, blank=True)
    is_published = models.BooleanField("Is published?", default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Submitted by"))


def work_image_upload_to(instance, filename):
    filename = unique_filename(filename)
    return 'uploads/resume/images/%s' % filename


class Work(ResumeBase):
    organization = models.CharField(_("Organization"), max_length=255)
    organization_image = models.ImageField(
        _("Organization logo"),
        upload_to=work_image_upload_to,
        width_field='width',
        height_field='height',
        null=True, blank=True)
    width = models.IntegerField(_("Image width"), null=True)
    height = models.IntegerField(_("Image height"), null=True)
    date_from = models.DateField(_("From"))
    date_till = models.DateField(_("Till"), null=True, blank=True)

    @property
    def primary_image(self):
        primary_image = WorkImage.objects.filter(work=self, is_published=True, is_primary=True)
        if primary_image:
            return primary_image.last()
        return None

    @property
    def images(self):
        images = WorkImage.objects.filter(work=self, is_published=True)
        if images:
            return images
        return None

    class Meta:
        verbose_name = _("Work experience")

    def __str__(self):
        return self.title


class WorkImage(models.Model):
    work = models.ForeignKey('Work')
    image = models.ImageField(
        _("Image"),
        width_field='width',
        height_field='height',
        upload_to=work_image_upload_to)
    width = models.IntegerField(_("Image width"), null=True)
    height = models.IntegerField(_("Image height"), null=True)
    is_primary = models.BooleanField(_("Primary Image?"), default=False)
    is_published = models.BooleanField("Is published?", default=False)
    datetime_added = models.DateTimeField(_("Date added"), auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Submitted by"))

    def save(self, *args, **kwargs):
        self.handle_primary_work_image()
        return super(WorkImage, self).save(*args, **kwargs)

    def handle_primary_work_image(self):
        primary_work_image = WorkImage.objects.filter(
            work=self.work,
            is_primary=True)

        if primary_work_image and self.is_primary:
            self.unset_previous_primary_work_image(primary_work_image)
        else:
            self.is_primary = True

    @staticmethod
    def unset_previous_primary_work_image(primary_work_image):
        primary_work_image.update(is_primary=False)


class Education(ResumeBase):
    date_from = models.DateField(_("From"), null=True, blank=True)
    date_till = models.DateField(_("Till"), null=True, blank=True)


class Interest(ResumeBase):
    pass
