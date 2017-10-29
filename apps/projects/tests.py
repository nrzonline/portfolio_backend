# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import IntegrityError
from django.test import TestCase, override_settings
import tempfile

from projects.factories import ProjectFactory

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
