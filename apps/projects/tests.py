# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import IntegrityError
from django.test import TestCase
from django.contrib.contenttypes.models import ContentType

from projects.factories import ProjectFactory
from multimedia.factories import ImageFactory, FileFactory, LinkFactory
from projects.serializers import ProjectListSerializer, ProjectDetailSerializer
from projects.viewsets import ProjectViewSet


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
        for is_published in [True, False]:
            ImageFactory.create(
                content_type=self.content_type,
                content_object=self.project,
                is_published=is_published)
        published_images = self.project.published_images
        self.assertEqual(len(published_images), 1)

    def test_project_multimedia_published_files(self):
        for is_published in [True, False]:
            FileFactory.create(
                content_type=self.content_type,
                content_object=self.project,
                is_published=is_published)
        published_files = self.project.published_files
        self.assertEqual(len(published_files), 1)

    def test_project_multimedia_published_links(self):
        for is_published in [True, False]:
            LinkFactory.create(
                content_type=self.content_type,
                content_object=self.project,
                is_published=is_published)
        published_links = self.project.published_links
        self.assertEqual(len(published_links), 1)


class TestProjectViewSets(TestCase):
    def setUp(self):
        self.project_view_set = ProjectViewSet()

    def test_project_view_set_list_uses_list_serializer(self):
        self.project_view_set.action = 'list'
        view_set_serializer_class = self.project_view_set.get_serializer_class()
        self.assertEqual(view_set_serializer_class, ProjectListSerializer)

    def test_project_view_set_detail_uses_detail_serializer(self):
        self.project_view_set.action = 'detail'
        view_set_serializer_class = self.project_view_set.get_serializer_class()
        self.assertEqual(view_set_serializer_class, ProjectDetailSerializer)
