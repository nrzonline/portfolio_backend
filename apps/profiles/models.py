# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import ugettext_lazy as _
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

from core.models.mixins import AuditMixin, PublishMixin, SlugMixin
from core.services import unique_filename


def profile_photo_upload_location(instance, filename):
    filename = unique_filename(filename)
    return 'uploads/projects/images/%s' % filename


class Profile(AuditMixin, PublishMixin, SlugMixin, models.Model):
    slugify_field = 'user'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(_("Screen shot"), upload_to=profile_photo_upload_location,
                              width_field='width', height_field='height',
                              null=True, blank=True)
    width = models.IntegerField(_("Image width"), null=True, blank=True)
    height = models.IntegerField(_("Image height"), null=True, blank=True)

    about = models.TextField(verbose_name=_("About"), max_length=10000, null=True, blank=True)
    first_name = models.CharField(_("First name"), max_length=50, null=True, blank=True)
    last_name = models.CharField(_("Last name"), max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(_("Date of birth"), null=True, blank=True)
    nationality = models.CharField(_("Nationality"), max_length=100, null=True, blank=True)
    location = models.CharField(_("Location"), max_length=100, null=True, blank=True)
    email = models.EmailField(_("E-mail address"), max_length=255, null=True, blank=True)
    phone_number = models.CharField(_("Phone number"), max_length=20, null=True, blank=True)
    occupation = models.CharField(_("Occupation"), max_length=255, null=True, blank=True)

    website_url = models.URLField(_("Personal website"), null=True, blank=True)
    linkedin_url = models.URLField(_("LinkedIn Url"), null=True, blank=True)
    facebook_url = models.URLField(_("Facebook Url"), null=True, blank=True)
    twitter_url = models.URLField(_("Twitter Url"), null=True, blank=True)
    stackoverflow_url = models.URLField(_("Stackoverflow Url"), null=True, blank=True)
    github_url = models.URLField(_("GitHub Url"), null=True, blank=True)

    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Modified by"),
                                    related_name="%(app_label)s_%(class)s_modified_related",
                                    null=True, blank=True)
    datetime_created = models.DateTimeField(_("Created on"), auto_now_add=True)
    datetime_modified = models.DateTimeField(_("Modified on"), null=True, blank=True)
    created_by = None

    def __str__(self):
        if self.first_name:
            return self.first_name
        return self.user.username

    def save(self, *args, **kwargs):
        if self.id:
            self.datetime_modified = datetime.now()
        return super(AuditMixin, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            created_by=instance.user,
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
        )
