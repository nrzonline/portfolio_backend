from django.utils.translation import ugettext as _
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from datetime import datetime


class ContentMixin(models.Model):
    title = models.CharField(_("Title"), max_length=50, unique=True)
    description = models.TextField(_("Description"), max_length=1500)
    content = models.TextField(_("Content body"), max_length=5000)

    class Meta:
        abstract = True


class AuditMixin(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Created by"),
                                   related_name="%(app_label)s_%(class)s_created_related")
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Modified by"),
                                    related_name="%(app_label)s_%(class)s_modified_related",
                                    null=True, blank=True)
    datetime_created = models.DateTimeField(_("Created on"), auto_now_add=True)
    datetime_modified = models.DateTimeField(_("Modified on"), null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.id:
            self.datetime_modified = datetime.now()
            self.modified_by = self.request.user
        else:
            self.created_by = self.request.user
        return super(AuditMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class PublishMixin(models.Model):
    is_published = models.BooleanField(_("Is published?"), default=False)
    datetime_published = models.DateTimeField(_("First published on"), null=True, blank=True)
    published_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("First published by"),
                                     related_name="%(app_label)s_%(class)s_publish_related",
                                     null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.is_published and not self.datetime_published:
            self.datetime_published = datetime.now()
        return super(PublishMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class SlugifyMixin(models.Model):
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(SlugifyMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True


