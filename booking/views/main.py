# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView, UpdateView

from ..forms import ReservationForm
from ..models import Reservation


@login_required
def index(request):
    """
    Index view with the calendar
    """
    context = {'title': _('Home')}
    return render(request, 'booking/index.html', context=context)


class ReservationCreate(LoginRequiredMixin, CreateView):
    """
    View to create a reservation
    """
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Create reservation')
        return context

    def form_valid(self, form):
        """
        Assign user and do not validate when creating
        """
        reservation = form.save(commit=False)
        reservation.in_charge = self.request.user
        reservation.validation = None
        return super().form_valid(form)


class ReservationUpdate(LoginRequiredMixin, UpdateView):
    """
    View to edit a reservation
    """
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Edit reservation')

        # Check user own reservation
        reservation = self.object
        if not reservation.in_charge == self.request.user:
            raise Http404

        # Warn user if the validation is already validated
        if reservation.validation:
            messages.add_message(self.request, messages.WARNING,
                                 _('By editing this reservation, '
                                   'it will be unvalidated!'))

        return context

    def form_valid(self, form):
        """
        Assign user and validation state when updating
        """
        reservation = form.save(commit=False)
        reservation.in_charge = self.request.user
        reservation.validation = None
        return super().form_valid(form)
