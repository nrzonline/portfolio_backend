# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
import os

from core.models.mixins import AuditMixin, PublishMixin, ContentTypeMixin
from core.services import unique_filename


def upload_image_location(instance, filename):
    filename = unique_filename(filename)
    location = os.path.join('uploads', 'images')
    return os.path.join(location, filename)


class Image(ContentTypeMixin, AuditMixin, PublishMixin):
    title = models.CharField(_("Image name"), max_length=50)
    description = models.CharField(_("Description"), max_length=1500)
    image = models.ImageField(_("Image"), upload_to=upload_image_location,
                              width_field='width', height_field='height')
    width = models.IntegerField(_("Image width"))
    height = models.IntegerField(_("Image height"))
    is_primary = models.BooleanField(_("Primary Image?"), default=False)

    def save(self, *args, **kwargs):
        self.update_object_primary_image()
        return super(Image, self).save(*args, **kwargs)

    def update_object_primary_image(self):
        object_primary_image = Image.objects.filter(
            content_type=self.content_type,
            object_id=self.object_id,
            is_primary=True)

        if object_primary_image and self.is_primary:
            object_primary_image.update(is_primary=False)
        else:
            self.is_primary = True


def upload_file_location(instance, filename):
    filename = unique_filename(filename)
    location = os.path.join('uploads', 'files')
    return os.path.join(location, filename)


class File(ContentTypeMixin, AuditMixin, PublishMixin):
    file = models.FileField(_("File"), upload_to=upload_file_location)
    title = models.CharField(_("File name"), max_length=50)
    description = models.CharField(_("Description"), max_length=1500)


class Link(ContentTypeMixin, AuditMixin, PublishMixin):
    title = models.CharField(_("Link name"), max_length=50)
    description = models.CharField(max_length=1500)
    url = models.URLField(_("Url"), max_length=255)
