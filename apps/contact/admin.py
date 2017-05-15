# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from contact.models import ContactDetail, ContactMessage
from contact.forms import ContactForm


class ContactDetailAdmin(admin.ModelAdmin):
    class Meta:
        model = ContactDetail

    exclude = ()
    list_display = ('first_name', 'last_name', 'email', 'phone_number',)


class ContactMessageAdmin(admin.ModelAdmin):
    class Meta:
        model = ContactMessage

    exclude = ('ip_address',)
    form = ContactForm


admin.site.register(ContactDetail, ContactDetailAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
