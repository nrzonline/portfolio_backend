# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, override_settings
from django.test.client import RequestFactory

from statistics.request_tracker import RequestTracker
from statistics.models import RequestCount


class TestRequestTracker(TestCase):
    def setUp(self):
        self.request_tracker = RequestTracker()
        self.preset_registrable_data = {
            'module': 'projects',
            'path': 'projects/1/slug-title',
            'ip_address': '127.0.0.1'
        }

        request_factory = RequestFactory()
        self.request = request_factory.get('/projects/1/slug-title/')

    def test_request_tracker_get_registrable_data_from_request(self):
        registrable_data = self.request_tracker.get_registrable_data_from_request(self.request)
        self.preset_registrable_data['ip_address'] = registrable_data['ip_address']
        self.assertEqual(registrable_data, self.preset_registrable_data)

    def test_request_tracker_extract_path_elements_from_url_path(self):
        path_elements = self.request_tracker.extract_path_elements(self.request.path)
        elements_expected = ['projects', '1', 'slug-title']
        self.assertEqual(path_elements, elements_expected)

    @override_settings(STATISTICS_IGNORED_MODULES=['admin'])
    def test_request_tracker_is_module_in_ignored_modules_list(self):
        is_module_ignored = self.request_tracker.is_module_in_ignored_modules_list('admin')
        self.assertTrue(is_module_ignored)

    @override_settings(STATISTICS_IGNORED_MODULES=[])
    def test_request_tracker_is_module_not_in_ignored_modules_list(self):
        is_module_ignored = self.request_tracker.is_module_in_ignored_modules_list('admin')
        self.assertFalse(is_module_ignored)

    def test_request_tracker_save_new_unique_request(self):
        self.request_tracker.save_request(self.preset_registrable_data)

        request_record = RequestCount.objects.get(
            module=self.preset_registrable_data['module'],
            path=self.preset_registrable_data['path'],
            ip_address=self.preset_registrable_data['ip_address'],
            hit_count=1
        )
        self.assertTrue(request_record)

    def test_request_tracker_increase_existing_request_count(self):
        self.request_tracker.save_request(self.preset_registrable_data)
        self.request_tracker.save_request(self.preset_registrable_data)

        request_record = RequestCount.objects.get(
            module=self.preset_registrable_data['module'],
            path=self.preset_registrable_data['path'],
            ip_address=self.preset_registrable_data['ip_address'],
        )
        self.assertEqual(request_record.hit_count, 2)

