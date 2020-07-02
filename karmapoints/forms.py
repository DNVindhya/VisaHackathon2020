from django import forms
from django.forms.utils import ValidationError

from accounts.models import ( Consumer, User, Card_Details)

class ConsumerUserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email')

class ConsumerDetailsEditForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = ('address','contact_number')

class ConsumerCardEditForm(forms.ModelForm):
    class Meta:
        model = Card_Details
        fields = ('account_number', 'expiry_data')
        #labels = { 'account_number' : 'Visa Card Number', 'expiry_data': 'Expiry Date'}
