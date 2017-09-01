# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from django.db import models


VOTE_CHOICES = (
    (0, 'LOVE'),
    (1, 'THUMBS_UP'),
    (2, 'THUMBS_DOWN'),
)


class Vote(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    vote = models.IntegerField(_("Vote rating"), choices=VOTE_CHOICES, default=0)

    comment = models.CharField(_("Comment"), max_length=2000, null=True, blank=True)
    name = models.CharField(_("Voter's name"), max_length=255, null=True, blank=True)
    email_address = models.EmailField(_("E-mail Address"), max_length=255, null=True, blank=True)

    ip_address = models.GenericIPAddressField(_("IP Address"), max_length=255)
    hide_comment = models.BooleanField(_("Hide comment"), default=False)
    cancel_vote = models.BooleanField(_("Cancel vote"), default=False)

    class Meta:
        unique_together = ('content_type', 'object_id', 'ip_address',)
