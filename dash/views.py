# -*- encoding: utf-8 -*-
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import DetailView, TemplateView

from base.view_utils import BaseMixin
from contact.views import ContactDetailMixin
from crm.models import Note, Ticket
from crm.service import get_contact_model
from invoice.models import TimeRecord
from report.views import ReportMixin


class ContactDetailView(
        LoginRequiredMixin, ContactDetailMixin, BaseMixin, DetailView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # crm
        try:
            crm_contact = self.object.crmcontact
        except ObjectDoesNotExist:
            crm_contact = None
        # invoice
        try:
            invoice_contact = self.object.invoicecontact
        except ObjectDoesNotExist:
            invoice_contact = None
        context.update(dict(
            crm_contact=crm_contact,
            invoice_contact=invoice_contact,
        ))
        return context


class DashView(
        LoginRequiredMixin, StaffuserRequiredMixin,
        ReportMixin, BaseMixin, TemplateView):
    """Dashboard includes the report mixin."""

    template_name = 'dash/dash.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(dict(
            notes=Note.objects.order_by('-pk')[:10],
            tickets=Ticket.objects.order_by('-pk')[:10],
            time_records=TimeRecord.objects.order_by('-pk')[:10],
        ))
        return context


class SettingsView(
        LoginRequiredMixin, StaffuserRequiredMixin,
        ReportMixin, BaseMixin, TemplateView):

    template_name = 'dash/settings.html'
