# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from base.view_utils import BaseMixin


class DashView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, TemplateView):

    template_name = 'dash/home.html'
