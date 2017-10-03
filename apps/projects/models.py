# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from core.services import unique_filename
from core.models.mixins import AuditMixin, PublishMixin, CompleteArticleMixin


class Project(CompleteArticleMixin):
    url = models.URLField(_("Project URL"), null=True, blank=True)
    skills = models.ManyToManyField('skills.Skill', verbose_name=_("Related skills"))

    @property
    def primary_image(self):
        primary_image = ProjectImage.objects.filter(project=self, is_primary=True)
        if primary_image:
            return primary_image.last()
        return None

    @property
    def published_images(self):
        return ProjectImage.objects.filter(project=self, is_published=True).order_by('-is_primary')

    @property
    def published_attachments(self):
        return ProjectAttachment.objects.filter(project=self, is_published=True)

    @property
    def published_links(self):
        return ProjectLink.objects.filter(project=self, is_published=True)

    def __str__(self):
        return self.title


def project_image_upload_location(instance, filename):
    filename = unique_filename(filename)
    return 'uploads/projects/images/%s' % filename


class ProjectImage(AuditMixin, PublishMixin):
    project = models.ForeignKey('Project')
    title = models.CharField(_("Image name"), max_length=50)
    description = models.CharField(_("Description"), max_length=1500)
    image = models.ImageField(_("Screenshot"), upload_to=project_image_upload_location,
                              width_field='width', height_field='height')
    width = models.IntegerField(_("Image width"))
    height = models.IntegerField(_("Image height"))
    is_primary = models.BooleanField(_("Primary Image?"), default=False)

    def save(self, *args, **kwargs):
        self.handle_primary_project_image()
        return super(ProjectImage, self).save(*args, **kwargs)

    def handle_primary_project_image(self):
        current_primary_project_image = ProjectImage.objects.filter(project=self.project, is_primary=True)

        if current_primary_project_image and self.is_primary:
            current_primary_project_image.update(is_primary=False)
        else:
            self.is_primary = True


def project_attachment_upload_location(instance, filename):
    filename = unique_filename(filename)
    return 'uploads/projects/attachments/%s' % filename


class ProjectAttachment(AuditMixin, PublishMixin):
    project = models.ForeignKey('Project')
    title = models.CharField(_("Attachment name"), max_length=50)
    description = models.CharField(_("Description"), max_length=1500)
    file = models.FileField(_("Attachment"), upload_to=project_attachment_upload_location)


class ProjectLink(AuditMixin, PublishMixin):
    project = models.ForeignKey('Project')
    title = models.CharField(_("Link name"), max_length=50)
    description = models.CharField( max_length=1500)
    url = models.URLField(_("Url"), max_length=255)
