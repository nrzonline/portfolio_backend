# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from contact.models import ContactMessage
from contact.forms import ContactForm


class ContactMessageAdmin(admin.ModelAdmin):
    class Meta:
        model = ContactMessage

    list_display = (
        'datetime_submitted',
        'subject',
        'name',
        'email',
        'phone_number',
        'organization',
        'ip_address',
    )
    exclude = ('ip_address',)
    form = ContactForm


admin.site.register(ContactMessage, ContactMessageAdmin)
