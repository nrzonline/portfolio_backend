# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, override_settings
from rest_framework.test import APITestCase
import tempfile

from skills.factories import SkillFactory, SkillCategoryFactory
from skills.models import skill_image_upload_location


TEMP_MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class TestSkillModel(TestCase):
    def test_skill_image_upload_location(self):
        filename = "image.png"
        upload_location = skill_image_upload_location(None, filename)

        self.assertTrue(upload_location.startswith(
            'uploads/skills/images/'))

    def test_skill_datetime_modified_on_update(self):
        skill = SkillFactory.create()
        self.assertEqual(skill.datetime_modified, None)

        skill.save()
        self.assertNotEqual(skill.datetime_modified, None)

    def test_skill_slug_updated_on_title_change(self):
        skill = SkillFactory.create()
        skill.title = "A new title"
        skill.save()

        self.assertEqual(skill.slug, "a-new-title")


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class TestSkillCategoryModel(TestCase):
    def test_skill_category_datetime_modified_on_update(self):
        category = SkillFactory.create()
        self.assertEqual(category.datetime_modified, None)

        category.save()
        self.assertNotEqual(category.datetime_modified, None)

    def test_skill_category_slug_updated_on_title_change(self):
        category = SkillCategoryFactory.create()
        category.title = "A new title"
        category.save()

        self.assertEqual(category.slug, "a-new-title")


class TestSkillsAPI(APITestCase):
    def test_skill_api_list_request(self):
        SkillFactory.create()
        response = self.client.get('/api/skills/')
        self.assertEqual(response.status_code, 200)

    def test_skill_api_detail_request(self):
        SkillFactory.create()
        response = self.client.get('/api/skills/1/')
        self.assertEqual(response.status_code, 200)

    def test_skill_category_api_list_request(self):
        SkillCategoryFactory.create()
        response = self.client.get('/api/skill-categories/')
        self.assertEqual(response.status_code, 200)

    def test_skill_category_api_detail_request(self):
        SkillCategoryFactory.create()
        response = self.client.get('/api/skill-categories/1/')
        self.assertEqual(response.status_code, 200)
