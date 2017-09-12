# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.utils.text import ugettext_lazy as _
from django.conf import settings


class Profile(models.Model):
    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    about = models.TextField(
        verbose_name=_("About"),
        max_length=10000)
    first_name = models.CharField(
        _("First name"),
        max_length=50)
    last_name = models.CharField(
        _("Last name"),
        max_length=50)
    date_of_birth = models.DateField(
        _("Date of birth"),
        null=True, blank=True)
    nationality = models.CharField(
        _("Nationality"),
        max_length=100,
        null=True, blank=True)
    location = models.CharField(
        _("Location"),
        max_length=100,
        null=True, blank=True)
    email = models.EmailField(
        _("E-mail address"),
        max_length=255,
        null=True, blank=True)
    phone_number = models.CharField(
        _("Phone number"),
        max_length=20,
        null=True, blank=True)
    occupation = models.CharField(
        _("Occupation"),
        max_length=255,
        null=True, blank=True)
    website_url = models.URLField(
        _("Personal website"),
        null=True, blank=True)
    linkedin_url = models.URLField(
        _("LinkedIn Url"),
        null=True, blank=True)
    facebook_url = models.URLField(
        _("Facebook Url"),
        null=True, blank=True)
    twitter_url = models.URLField(
        _("Twitter Url"),
        null=True, blank=True)
    stackoverflow_url = models.URLField(
        _("Stackoverflow Url"),
        null=True, blank=True)
    github_url = models.URLField(
        _("GitHub Url"),
        null=True, blank=True)
    datetime_modified = models.DateTimeField(
        auto_now_add=True)

    def __unicode__(self):
        return self.first_name


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            account=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
        )

post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)
