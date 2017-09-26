# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from users.factories import UserFactory

from profiles.models import Profile


class TestProfileModel(TestCase):
    def test_profile_create_on_user_creation(self):
        user = UserFactory.create()
        profile = Profile.objects.get(account=user)

        self.assertTrue(profile.account, user)


