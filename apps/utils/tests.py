# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from utils import services


class TestUtilities(TestCase):
    def test_random_string(self):
        random_string = services.random_string(15)
        self.assertEqual(len(random_string), 15)

    def test_unique_filename_keeps_proper_filename_layout(self):
        filename = "file_name"
        file_extension = ".tar.gz"
        full_filename = '%s%s' % (filename, file_extension)
        unique_filename = services.unique_filename(full_filename)

        self.assertTrue(filename in unique_filename)
        self.assertTrue(unique_filename.endswith(file_extension))

    def test_unique_file_name(self):
        filename = "file_name.tar.gz"
        unique_filename_a = services.unique_filename(filename)
        unique_filename_b = services.unique_filename(filename)
        self.assertNotEqual(unique_filename_a, unique_filename_b)

