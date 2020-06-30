import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class PaymentForm(forms.Form):
    # Input fields for the get the details required to initiate payment
    # Update validation for these fields
    account_nickname = forms.CharField(max_length=200,strip="True")
    account_holder = forms.CharField(max_length=300,strip="True")
    card_number = forms.IntegerField(min_value=4000000000000000,max_value=4999999999999999)
    expiration_date = forms.CharField(max_length=200,strip="True")
    billing_address = forms.CharField(max_length=400,strip="True")
    city = forms.CharField(max_length=100,strip="True")
    country = forms.CharField(max_length=50,strip="True")
    postal_code = forms.IntegerField(min_value=10000,max_value=99999)
    payment_amount = forms.FloatField(min_value=1,max_value=40000)


    def clean_offer_data(self):
        # Sanitising data
        account_nickname = self.cleaned_data['account_nickname']
        account_holder = self.cleaned_data['account_holder']
        card_number = self.cleaned_data['card_number']
        expiration_date = self.cleaned_data['expiration_date']
        billing_address = self.cleaned_data['billing_address']
        city = self.cleaned_data['city']
        country = self.cleaned_data['country']
        postal_code = self.cleaned_data['postal_code']
        payment_amount = self.cleaned_data['payment_amount']

        error_messages = []

        # Check if karma points is neither too high nor too low
        # if karma_points < 1 or karma_points > 100000:
        #     error_messages.append('Invalid value for karma points')
        #     self._errors["karma_points"] = "Please enter a valid value for karma points"

        # # Check if start date is not in the past. 
        # if start_date < datetime.date.today():
        #     error_messages.append('Offer cannot be started before today')
        #     self._errors["start_date"] = "Please enter a valid vdate for karma points to start"

        # if len(error_messages):
        #     raise forms.ValidationError(' & '.join(error_messages))

        return self.cleaned_data