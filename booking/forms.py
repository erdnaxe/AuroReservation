from django import forms
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
        When validating, check that there is no reservation at that time
        """
        form_data = self.cleaned_data
        validation = form_data.get('validation')
        if validation:
            start_time = form_data['start_time']
            end_time = form_data['end_time']

            reservation_list = form_data['room'].reservation_set.filter(
                validation=True,
                start_time__lt=end_time,
                end_time__gt=start_time,
            ).exclude(pk=self.instance.pk)

            if reservation_list.exists():
                raise forms.ValidationError(
                    _("There is already a reservation at this time."))

        return form_data

    def clean_end_time(self):
        """
        Check that end time is after start time
        """
        form_data = self.cleaned_data
        start_time = form_data['start_time']
        end_time = form_data['end_time']
        if start_time > end_time:
            raise forms.ValidationError(
                _("Reservation must end after it begins.")
            )

        return form_data['end_time']


class ReservationForm(ReservationAdminForm):
    """
    Reservation form in public site
    """
    class Meta:
        model = Reservation
        exclude = ('in_charge', 'validation')

    # TODO: if already validated then warn
