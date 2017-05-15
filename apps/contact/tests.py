# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APITestCase

from contact.factories import ContactDetailFactory, ContactMessageFactory
from contact.forms import ContactForm


class TestContactForm(TestCase):
    def test_empty_contact_form_is_invalid(self):
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())

    def test_contact_form_with_filled_required_fields_is_valid(self):
        form_data = ContactMessageFactory.as_form_data()
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())


class TestSkillsAPI(APITestCase):
    def test_contact_detail_api_request(self):
        ContactDetailFactory.create()
        response = self.client.get('/api/contact/1/')
        self.assertEqual(response.status_code, 200)

    def test_contact_get_returns_405_method_not_allowed(self):
        response = self.client.get('/api/contact-messages/')
        self.assertEqual(response.status_code, 405)

    def test_contact_message_form_submit(self):
        contact_message_form_data = ContactMessageFactory.as_form_data()
        response = self.client.post(
            '/api/contact-messages/',
            contact_message_form_data,
            format='json',
            **{
                'REMOTE_ADDR': '127.0.0.1',
                'REMOTE_HOST': 'localhost',
            })
        self.assertEqual(response.status_code, 201)
