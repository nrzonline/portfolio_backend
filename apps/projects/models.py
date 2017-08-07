# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext as _

from utils.services import unique_filename


class Project(models.Model):
    title = models.CharField(
        _("Project title"),
        max_length=50,
        unique=True)
    short_description = models.TextField(
        _("Short description"),
        max_length=1500)
    full_description = models.TextField(
        _("Full description"),
        max_length=5000)
    url = models.URLField(
        _("Project URL"),
        null=True, blank=True)
    is_published = models.BooleanField(
        _("Is published?"))
    skills = models.ManyToManyField('skills.Skill')
    datetime_added = models.DateTimeField(
        _("Added on"),
        auto_now_add=True)
    datetime_modified = models.DateTimeField(
        _("Updated on"),
        null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Author"))
    slug = models.SlugField()

    def published_images(self):
        images = ProjectImage.objects.filter(
            project=self, 
            is_published=True).order_by('-is_primary')
        return images

    def published_attachments(self):
        images = ProjectAttachment.objects.filter(
            project=self,
            is_published=True)
        return images

    def published_links(self):
        links = ProjectLink.objects.filter(
            project=self,
            is_published=True)
        return links

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.id:
            self.datetime_modified = datetime.now()
        return super(Project, self).save(*args, **kwargs)


def project_image_upload_location(instance, filename):
    filename = unique_filename(filename)
    return 'uploads/projects/images/%s' % filename


class ProjectImage(models.Model):
    project = models.ForeignKey(
        'Project')
    title = models.CharField(
        _("Image name"),
        max_length=50)
    description = models.CharField(
        _("Description"),
        max_length=1500)
    image = models.ImageField(
        _("Screenshot"),
        width_field='width',
        height_field='height',
        upload_to=project_image_upload_location)
    width = models.IntegerField(
        _("Image width"))
    height = models.IntegerField(
        _("Image height"))
    is_primary = models.BooleanField(
        _("Primary Image?"),
        default=False)
    is_published = models.BooleanField(
        _("Is published?"))
    datetime_added = models.DateTimeField(
        _("Added on"),
        auto_now_add=True)
    datetime_modified = models.DateTimeField(
        _("Updated on"),
        null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Submitted by"))
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.update_datetime_modified()
        self.handle_primary_project_image()
        return super(ProjectImage, self).save(*args, **kwargs)

    def update_datetime_modified(self):
        if self.id:
            self.datetime_modified = datetime.now()

    def handle_primary_project_image(self):
        primary_project_image = ProjectImage.objects.filter(
            project=self.project,
            is_primary=True)

        if primary_project_image and self.is_primary:
            self.unset_previous_primary_project_image(primary_project_image)
        else:
            self.is_primary = True

    @staticmethod
    def unset_previous_primary_project_image(primary_project_image):
        primary_project_image.update(is_primary=False)


def project_attachment_upload_location(instance, filename):
    filename = unique_filename(filename)
    return 'uploads/projects/attachments/%s' % filename


class ProjectAttachment(models.Model):
    project = models.ForeignKey(
        'Project')
    title = models.CharField(
        _("Attachment name"),
        max_length=50)
    description = models.CharField(
        _("Description"),
        max_length=1500)
    file = models.FileField(
        _("Attachment"),
        upload_to=project_attachment_upload_location)
    is_published = models.BooleanField(
        _("Is published?"))
    datetime_added = models.DateTimeField(
        _("Added on"),
        auto_now_add=True)
    datetime_modified = models.DateTimeField(
        _("Updated on"),
        null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Submitted by"))
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.update_datetime_modified()
        return super(ProjectAttachment, self).save(*args, **kwargs)

    def update_datetime_modified(self):
        if self.id:
            self.datetime_modified = datetime.now()


class ProjectLink(models.Model):
    project = models.ForeignKey(
        'Project')
    title = models.CharField(
        _("Link name"),
        max_length=50)
    description = models.CharField(
        max_length=1500)
    url = models.URLField(
        _("Url"),
        max_length=255)
    is_published = models.BooleanField(
        _("Is published?"))
    datetime_added = models.DateTimeField(
        _("Added on"),
        auto_now_add=True)
    datetime_modified = models.DateTimeField(
        _("Updated on"),
        null=True, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Added by"))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.update_datetime_modified()
        return super(ProjectLink, self).save(*args, **kwargs)

    def update_datetime_modified(self):
        if self.id:
            self.datetime_modified = datetime.now()
