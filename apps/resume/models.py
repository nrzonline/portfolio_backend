# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.services import unique_filename
from core.models.mixins import ContentMixin, AuditMixin, PublishMixin


class ResumeBase(ContentMixin, AuditMixin, PublishMixin):
    pass


def work_image_upload_to(instance, filename):
    filename = unique_filename(filename)
    return 'uploads/resume/images/%s' % filename


class Work(ResumeBase):
    organization = models.CharField(_("Organization"), max_length=255)
    organization_image = models.ImageField(_("Organization logo"), upload_to=work_image_upload_to,
                                           width_field='width', height_field='height',
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


class WorkImage(AuditMixin, PublishMixin):
    work = models.ForeignKey('Work')
    title = models.CharField(_("Image name"), max_length=50)
    description = models.CharField(_("Description"), max_length=1500)
    image = models.ImageField(_("Image"), upload_to=work_image_upload_to,
                              width_field='width', height_field='height')
    width = models.IntegerField(_("Image width"), null=True)
    height = models.IntegerField(_("Image height"), null=True)
    is_primary = models.BooleanField(_("Primary Image?"), default=False)

    def save(self, *args, **kwargs):
        self.handle_primary_work_image()
        return super(WorkImage, self).save(*args, **kwargs)

    def handle_primary_work_image(self):
        primary_work_image = WorkImage.objects.filter(
            work=self.work,
            is_primary=True)

        if primary_work_image and self.is_primary:
            primary_work_image.update(is_primary=False)
        else:
            self.is_primary = True


class Education(ResumeBase):
    date_from = models.DateField(_("From"), null=True, blank=True)
    date_till = models.DateField(_("Till"), null=True, blank=True)


class Interest(ResumeBase):
    pass
