# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import IntegrityError
from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
import tempfile

from projects.factories import ProjectFactory
from multimedia.factories import ImageFactory, FileFactory, LinkFactory

TEMP_MEDIA_ROOT = tempfile.mkdtemp()


class TestProjectModel(TestCase):
    def setUp(self):
        self.project = ProjectFactory.create()
        self.content_type = ContentType.objects.get(
            app_label='projects', model='project')

    def test_project_unique_title(self):
        project_b = ProjectFactory.create(title="other title")
        project_b.title = self.project.title

        with self.assertRaises(IntegrityError):
            project_b.save()

    def test_project_datetime_modified_on_update(self):
        self.assertEqual(self.project.datetime_modified, None)
        self.project.save()
        self.assertNotEqual(self.project.datetime_modified, None)

    def test_project_slug_updated_on_title_change(self):
        self.project.title = "A new title"
        self.project.save()
        self.assertEqual(self.project.slug, "a-new-title")

    def test_project_multimedia_primary_image(self):
        ImageFactory.create(
            content_type=self.content_type,
            content_object=self.project,
            is_published=True)
        primary_image = self.project.primary_image
        self.assertTrue(primary_image)

    def test_project_multimedia_published_images(self):
        ImageFactory.create(
            content_type=self.content_type,
            content_object=self.project,
            is_published=True)
        published_images = self.project.published_images
        self.assertEqual(len(published_images), 1)

    def test_project_multimedia_published_files(self):
        FileFactory.create(
            content_type=self.content_type,
            content_object=self.project,
            is_published=True)
        published_files = self.project.published_files
        self.assertEqual(len(published_files), 1)

    def test_project_multimedia_published_links(self):
        LinkFactory.create(
            content_type=self.content_type,
            content_object=self.project,
            is_published=True)
        published_links = self.project.published_links
        self.assertEqual(len(published_links), 1)
