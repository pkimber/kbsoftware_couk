# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase
from login.tests.scenario import default_scenario_login


class TestViewPerm(PermTestCase):

    def setUp(self):
        default_scenario_login()

    def test_dash(self):
        self._assert_staff(reverse('project.home.user'))

    def test_home(self):
        self.assert_any(reverse('project.home'))

    def test_login(self):
        self.assert_any(reverse('login'))
