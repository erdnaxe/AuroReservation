from django import forms
from .models import Reservation
from django.utils.translation import gettext_lazy as _

class ReservationAdminForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ()

    def clean(self):
        form_data = self.cleaned_data

        validation = form_data['validation']

        if validation:

            start_time = form_data['start_time']
            end_time = form_data['end_time']
            if start_time > end_time:
                raise forms.ValidationError(_("Reservation must end after it begins."))

            reservation_list = form_data['room'].reservation_set.filter(
                validation=True, 
                start_time__lt=end_time, 
                end_time__gt=start_time,
            ).exclude(pk=self.instance.pk)
            
            if reservation_list.exists():
                raise forms.ValidationError(_("There is already a reservation at this time."))

        return form_data