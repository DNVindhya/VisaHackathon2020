import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class CreateUpdateOfferForm(forms.Form):
    # Input fields for the Create and Update Offer forms
    offer_name = forms.CharField(max_length=200,strip="True")
    karma_points = forms.IntegerField(min_value=1,max_value=100000)
    percent_off = forms.IntegerField(min_value=1,max_value=99)
    start_date = forms.DateField(initial=datetime.date.today)
    validity = forms.IntegerField(min_value=1,max_value=365)
    details = forms.CharField(max_length=200,strip="True")

    def clean_offer_data(self):
        # Sanitising data
        offer_name = self.cleaned_data['offer_name']
        karma_points = self.cleaned_data['karma_points']
        percent_off = self.cleaned_data['percent_off']
        start_date = self.cleaned_data['start_date']
        validity = self.cleaned_data['validity']
        details = self.cleaned_data['details']

        error_messages = []

        # Check if karma points is neither too high nor too low
        if karma_points < 1 or karma_points > 100000:
            error_messages.append('Invalid value for karma points')
            self._errors["karma_points"] = "Please enter a valid value for karma points"

        # Check if start date is not in the past. 
        if start_date < datetime.date.today():
            error_messages.append('Offer cannot be started before today')
            self._errors["start_date"] = "Please enter a valid vdate for karma points to start"

        if len(error_messages):
            raise forms.ValidationError(' & '.join(error_messages))

        return self.cleaned_data