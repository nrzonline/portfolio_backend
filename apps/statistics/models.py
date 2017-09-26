# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class RequestCount(models.Model):
    module = models.CharField(_("Module"), max_length=255)
    path = models.CharField(_("Path"), max_length=255, null=True, blank=True)
    ip_address = models.GenericIPAddressField(_("IP Address"), max_length=255)
    hit_count = models.IntegerField(_("Hit count"), default=1)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
