# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APITestCase

from contact.factories import ContactMessageFactory
from contact.forms import ContactForm


class TestContactForm(TestCase):
    def test_empty_contact_form_is_invalid(self):
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())

    def test_contact_form_with_filled_required_fields_is_valid(self):
        form_data = ContactMessageFactory.as_form_data()
        form = ContactForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())


class TestContactAPI(APITestCase):
    def test_contact_get_returns_405_method_not_allowed(self):
        response = self.client.get('/contact-message/')
        self.assertEqual(response.status_code, 405)

    def test_contact_message_form_submit(self):
        contact_message_form_data = ContactMessageFactory.as_form_data()
        response = self.client.post(
            '/contact-message/',
            contact_message_form_data,
            format='json',
            **{
                'REMOTE_ADDR': '127.0.0.1',
                'REMOTE_HOST': 'localhost',
            }
        )
        self.assertEqual(response.status_code, 201)
