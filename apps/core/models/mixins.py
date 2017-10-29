from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext as _
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class ContentTypeMixin(models.Model):
    class Meta:
        abstract = True

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class ContentMixin(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(_("Title"), max_length=50, unique=True)
    description = models.TextField(_("Description"), max_length=1500)
    content = models.TextField(_("Content body"), max_length=5000)


class AuditMixin(models.Model):
    class Meta:
        abstract = True

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
        return super(AuditMixin, self).save(*args, **kwargs)


class PublishMixin(models.Model):
    class Meta:
        abstract = True

    is_published = models.BooleanField(_("Is published?"), default=False)
    datetime_published = models.DateTimeField(_("First published on"), null=True, blank=True)
    published_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("First published by"),
                                     related_name="%(app_label)s_%(class)s_publish_related",
                                     null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.is_published and not self.datetime_published:
            self.datetime_published = datetime.now()
        return super(PublishMixin, self).save(*args, **kwargs)


class SlugMixin(models.Model):
    class Meta:
        abstract = True

    slugify_field = 'title'
    slug = models.SlugField()

    def get_slug(self):
        try:
            slugify_field_value = getattr(self, self.slugify_field)
        except AttributeError:
            raise AttributeError("Field '%s' was marked as field to be used as slug, but does not exist in '%s'" %
                                 (self.slugify_field, self.__class__.__name__))
        return slugify(slugify_field_value)

    def save(self, *args, **kwargs):
        self.slug = self.get_slug()
        return super(SlugMixin, self).save(*args, **kwargs)


class VoteMixin(models.Model):
    class Meta:
        abstract = True

    votes = GenericRelation('votes.Vote')


class CompleteArticleMixin(ContentMixin, AuditMixin, PublishMixin, SlugMixin, VoteMixin):
    class Meta:
        abstract = True
