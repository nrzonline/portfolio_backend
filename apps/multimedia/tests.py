# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, override_settings
import tempfile

from multimedia.models import Image, File, upload_file_location, upload_image_location
from multimedia.factories import ImageFactory, FileFactory, LinkFactory

TEMP_MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class TestProjectImageModel(TestCase):
    def test_image_upload_to_location(self):
        filename = "filename.jpg"
        upload_location = upload_image_location(None, filename)

        self.assertTrue(upload_location.startswith('uploads/images/'))

    def test_first_objects_image_is_always_primary(self):
        project_image = ImageFactory.create()
        project_image.title = "project image"
        project_image.is_primary = False
        project_image.save()

        project_image = Image.objects.get(title="project image")
        self.assertTrue(project_image.is_primary)

    def test_objects_image_unset_previous_primary(self):
        project_image = ImageFactory.create()
        project_image.title = "project image"
        project_image.save()
        ImageFactory.create(is_primary=True)

        project_image = Image.objects.get(title="project image")
        self.assertFalse(project_image.is_primary)

    def test_image_datetime_modified_on_update(self):
        project_image = ImageFactory.create()
        self.assertEqual(project_image.datetime_modified, None)

        project_image.save()
        self.assertNotEqual(project_image.datetime_modified, None)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class TestFileModel(TestCase):
    def test_file_upload_location(self):
        filename = "file.pdf"
        upload_location = upload_file_location(None, filename)
        self.assertTrue(upload_location.startswith('uploads/files/'))

    def test_datetime_modified_on_update(self):
        upload_file = FileFactory.create()
        self.assertEqual(upload_file.datetime_modified, None)

        upload_file.save()
        self.assertNotEqual(upload_file.datetime_modified, None)


class TestLinkModel(TestCase):
    def test_link_datetime_modified_on_update(self):
        project_link = LinkFactory.create()
        self.assertEqual(project_link.datetime_modified, None)

        project_link.save()
        self.assertNotEqual(project_link.datetime_modified, None)
