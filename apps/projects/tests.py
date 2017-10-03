# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import IntegrityError
from django.test import TestCase, override_settings
import tempfile

from projects.factories import (
     ProjectFactory, ProjectImageFactory, ProjectAttachmentFactory, ProjectLinkFactory)
from projects.models import (
     ProjectImage, project_image_upload_location, project_attachment_upload_location)

TEMP_MEDIA_ROOT = tempfile.mkdtemp()


class TestProjectModel(TestCase):
    def test_project_unique_title(self):
        project_a = ProjectFactory.create()
        project_b = ProjectFactory.create(title="other title")
        project_b.title = project_a.title

        with self.assertRaises(IntegrityError):
            project_b.save()

    def test_project_datetime_modified_on_update(self):
        project = ProjectFactory.create()
        self.assertEqual(project.datetime_modified, None)

        project.save()
        self.assertNotEqual(project.datetime_modified, None)

    def test_project_slug_updated_on_title_change(self):
        project = ProjectFactory.create()
        project.title = "A new title"
        project.save()

        self.assertEqual(project.slug, "a-new-title")


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class TestProjectImageModel(TestCase):
    def test_project_image_upload_to_location(self):
        filename = "filename.jpg"
        upload_location = project_image_upload_location(None, filename)

        self.assertTrue(upload_location.startswith('uploads/projects/images/'))

    def test_first_project_image_always_primary(self):
        project_image = ProjectImageFactory.create()
        project_image.title = "project image"
        project_image.is_primary = False
        project_image.save()

        project_image = ProjectImage.objects.get(title="project image")
        self.assertTrue(project_image.is_primary)

    def test_project_image_unset_previous_primary(self):
        project_image = ProjectImageFactory.create()
        project_image.title = "project image"
        project_image.save()
        ProjectImageFactory.create(is_primary=True)

        project_image = ProjectImage.objects.get(title="project image")
        self.assertFalse(project_image.is_primary)

    def test_project_image_datetime_modified_on_update(self):
        project_image = ProjectImageFactory.create()
        self.assertEqual(project_image.datetime_modified, None)

        project_image.save()
        self.assertNotEqual(project_image.datetime_modified, None)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class TestProjectAttachmentModel(TestCase):
    def test_project_attachment_upload_location(self):
        filename = "attachment.pdf"
        upload_location = project_attachment_upload_location(None, filename)

        self.assertTrue(upload_location.startswith('uploads/projects/attachments/'))

    def test_project_attachment_datetime_modified_on_update(self):
        project_attachment = ProjectAttachmentFactory.create()
        self.assertEqual(project_attachment.datetime_modified, None)

        project_attachment.save()
        self.assertNotEqual(project_attachment.datetime_modified, None)


class TestProjectLinkModel(TestCase):
    def test_project_link_datetime_modified_on_update(self):
        project_link = ProjectLinkFactory.create()
        self.assertEqual(project_link.datetime_modified, None)

        project_link.save()
        self.assertNotEqual(project_link.datetime_modified, None)
