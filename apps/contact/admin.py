# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from contact.models import ContactMessage
from contact.forms import ContactForm


class ContactMessageAdmin(admin.ModelAdmin):
    class Meta:
        model = ContactMessage

    exclude = ('ip_address',)
    form = ContactForm


admin.site.register(ContactMessage, ContactMessageAdmin)
