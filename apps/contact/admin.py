# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext as _

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

    fieldsets = (
        (_('Contact details'), {
            'fields': (
                'name',
                'email',
                'phone_number',
                'organization',
            )
        }),
        (_('Message'), {
            'fields': (
                'subject',
                'message',
            )
        }),
    )


admin.site.register(ContactMessage, ContactMessageAdmin)
