# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import IntegrityError
from django.test import TestCase, override_settings
from rest_framework.test import APITestCase
import tempfile

from projects.factories import ProjectFactory, ProjectImageFactory, \
    ProjectAttachmentFactory, ProjectLinkFactory
from projects.models import ProjectImage, \
    project_image_upload_location, project_attachment_upload_location


TEMP_MEDIA_ROOT = tempfile.mkdtemp()


class TestProjectModel(TestCase):
    def test_project_unique_project_title(self):
        project_a = ProjectFactory.create()
        project_b = ProjectFactory.build()
        project_b.name = project_a.title

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

        self.assertTrue(upload_location.startswith(
            'uploads/projects/images/'))

    def test_first_project_image_always_primary(self):
        project_image = ProjectImageFactory.create()
        project_image.title = "project_image"
        project_image.is_primary = False
        project_image.save()

        project_image = ProjectImage.objects.get(title="project_image")
        self.assertTrue(project_image.is_primary)

    def test_project_image_unset_previous_primary(self):
        project_image_a = ProjectImageFactory.create()
        project_image_a.title = "project_image_a"
        project_image_a.save()
        ProjectImageFactory.create()

        project_image_a = ProjectImage.objects.get(
            title="project_image_a")
        self.assertFalse(project_image_a.is_primary)

    def test_project_image_datetime_modified_on_update(self):
        project_image = ProjectImageFactory.create()
        self.assertEqual(project_image.datetime_modified, None)

        project_image.save()
        self.assertNotEqual(project_image.datetime_modified, None)

    def test_project_image_slug_updated_on_title_change(self):
        project_image = ProjectImageFactory.create()
        project_image.title = "A new title"
        project_image.save()

        self.assertEqual(project_image.slug, "a-new-title")


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class TestProjectAttachmentModel(TestCase):
    def test_project_attachment_upload_location(self):
        filename = "attachment.pdf"
        upload_location = project_attachment_upload_location(None, filename)

        self.assertTrue(upload_location.startswith(
            'uploads/projects/attachments/'))

    def test_project_attachment_datetime_modified_on_update(self):
        project_attachment = ProjectAttachmentFactory.create()
        self.assertEqual(project_attachment.datetime_modified, None)

        project_attachment.save()
        self.assertNotEqual(project_attachment.datetime_modified, None)

    def test_project_attachment_slug_updated_on_title_change(self):
        project_attachment = ProjectAttachmentFactory.create()
        project_attachment.title = "A new title"
        project_attachment.save()

        self.assertEqual(project_attachment.slug, "a-new-title")


class TestProjectLinkModel(TestCase):
    def test_project_link_datetime_modified_on_update(self):
        project_link = ProjectLinkFactory.create()
        self.assertEqual(project_link.datetime_modified, None)

        project_link.save()
        self.assertNotEqual(project_link.datetime_modified, None)


class TestProjectsAPI(APITestCase):
    def test_project_api_list_request(self):
        ProjectFactory.create()
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, 200)

    def test_project_api_detail_request(self):
        ProjectFactory.create()
        response = self.client.get('/api/projects/1/')
        self.assertEqual(response.status_code, 200)

    def test_project_image_list_request(self):
        ProjectImageFactory.create()
        response = self.client.get('/api/project-images/')
        self.assertEqual(response.status_code, 200)

    def test_project_image_detail_request(self):
        ProjectImageFactory.create()
        response = self.client.get('/api/project-images/1/')
        self.assertEqual(response.status_code, 200)

    def test_project_attachment_detail_request(self):
        ProjectAttachmentFactory.create()
        response = self.client.get('/api/project-attachments/')
        self.assertEqual(response.status_code, 200)

    def test_project_attachment_list_request(self):
        ProjectAttachmentFactory.create()
        response = self.client.get('/api/project-attachments/1/')
        self.assertEqual(response.status_code, 200)

    def test_project_link_list_request(self):
        ProjectLinkFactory.create()
        response = self.client.get('/api/project-links/')
        self.assertEqual(response.status_code, 200)

    def test_project_link_detail_request(self):
        ProjectLinkFactory.create()
        response = self.client.get('/api/project-links/1/')
        self.assertEqual(response.status_code, 200)
