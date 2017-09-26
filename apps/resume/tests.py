# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, override_settings
from django.db import IntegrityError
import tempfile

from resume.factories import WorkFactory, WorkImageFactory, EducationFactory, InterestFactory
from resume.models import WorkImage, work_image_upload_location

TEMP_MEDIA_ROOT = tempfile.mkdtemp()


class TestWorkModel(TestCase):
    def test_work_unique_title(self):
        work_a = WorkFactory.create()
        work_b = WorkFactory.create(title="different title")
        work_b.title = work_a.title

        with self.assertRaises(IntegrityError):
            work_b.save()

    def test_work_datetime_modified_on_update(self):
        work = WorkFactory.create()
        self.assertEqual(work.datetime_modified, None)

        work.save()
        self.assertNotEqual(work.datetime_modified, None)

    def test_work_datetime_published_on_publish(self):
        work_image = WorkImageFactory.create(is_published=True)
        self.assertNotEqual(work_image.datetime_published, None)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class TestWorkImageModel(TestCase):
    def test_project_image_upload_to_location(self):
        filename = "filename.jpg"
        upload_location = work_image_upload_location(None, filename)

        self.assertTrue(upload_location.startswith('uploads/resume/images/'))

    def test_first_work_image_always_primary(self):
        work_image = WorkImageFactory.create(title="title")
        self.assertTrue(work_image.is_primary)

    def test_work_image_unset_previous_primary(self):
        work_image = WorkImageFactory.create(title="title")
        self.assertTrue(work_image.is_primary)

        WorkImageFactory.create(is_primary=True)
        work_image = WorkImage.objects.get(title="title")
        self.assertFalse(work_image.is_primary)

    def test_work_image_datetime_modified_on_update(self):
        work_image = WorkImageFactory.create()
        self.assertEqual(work_image.datetime_modified, None)

        work_image.save()
        self.assertNotEqual(work_image.datetime_modified, None)

    def test_work_image_datetime_published_on_publish(self):
        work_image = WorkImageFactory.create(is_published=True)
        self.assertNotEqual(work_image.datetime_published, None)


class TestEducationModel(TestCase):
    def test_education_datetime_modified_on_update(self):
        education = EducationFactory.create()
        self.assertEqual(education.datetime_modified, None)

        education.save()
        self.assertNotEqual(education.datetime_modified, None)

    def test_education_datetime_published_on_publish(self):
        education = EducationFactory.create(is_published=True)
        self.assertNotEqual(education.datetime_published, None)


class TestInterestModel(TestCase):
    def test_interest_datetime_modified_on_update(self):
        interest = InterestFactory.create()
        self.assertEqual(interest.datetime_modified, None)

        interest.save()
        self.assertNotEqual(interest.datetime_modified, None)

    def test_interest_datetime_published_on_publish(self):
        interest = InterestFactory.create(is_published=True)
        self.assertNotEqual(interest.datetime_published, None)
