# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _


class ContactMessage(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=255)
    organization = models.CharField(
        _("Organisation name"),
        max_length=255,
        null=True, blank=True)
    email = models.EmailField(
        _("E-mail address"))
    phone_number = models.CharField(
        _("Phone number"),
        max_length=20,
        null=True, blank=True)
    subject = models.CharField(
        _("Contact subject"),
        max_length=255)
    message = models.CharField(
        _("Contact message"),
        max_length=5000)
    datetime_submitted = models.DateTimeField(
        _("Datetime of submission"),
        auto_now_add=True)
    ip_address = models.GenericIPAddressField(
        _("Submitters IP-Address"))
