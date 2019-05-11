# -*- mode: python; coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0-or-later

from django import forms
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .models import Reservation


class ReservationAdminForm(forms.ModelForm):
    """
    Reservation form in admin
    """

    class Meta:
        model = Reservation
        exclude = ()

    def clean(self):
        """
        Check global form constraints
        """
        form_data = self.cleaned_data
        validation = form_data.get('validation')
        start_time = form_data['start_time']
        end_time = form_data['end_time']

        # When validating, check that there is no reservation at that time
        if validation:
            reservation_list = form_data['room'].reservation_set.filter(
                validation=True,
                start_time__lt=end_time,
                end_time__gt=start_time,
            ).exclude(pk=self.instance.pk)

            if reservation_list.exists():
                raise forms.ValidationError(
                    _("There is already a reservation at this time."))

        # Check that end time is after start time
        if start_time > end_time:
            raise forms.ValidationError(
                _("Reservation must end after it begins.")
            )

        # Check that start time is not in the past
        now = timezone.now()
        if now > start_time:
            raise forms.ValidationError(
                _("You can't make a reservation in the past."))

        return form_data

    def clean_in_charge(self):
        """
        Limit how many reservations an user can own
        """
        in_charge = self.cleaned_data['in_charge']
        now = timezone.now()
        user_reservations = in_charge.reservation_set.filter(
            start_time__gt=now,
        )
        # TODO put this constant in app config
        if user_reservations.count() >= 10:
            raise forms.ValidationError(
                _("You already have to many future reservations."))
        return in_charge


class ReservationForm(ReservationAdminForm):
    """
    Reservation form in public site
    """

    class Meta:
        model = Reservation
        exclude = ('in_charge', 'validation')
