from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from accounts.models import ( Consumer, Merchant, User, Card_Details)

# COUNTRY_CHOICES =[
#     ("1", "United States ")   
# ] 

STATE_CHOICES =(
    ('', 'Choose...'),
    ('CF', 'California'),
    ('NY', 'New York')
)

COUNTRY_CHOICES =(
    ('', 'Choose...'),
    ('US', 'United States'),
)
class MerchantSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'email')
        labels = { 'first_name' : 'Store Name'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_merchant = True
        if commit:
            user.save()
            Merchant.objects.create(user=user)
        return user


class ConsumerSignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_consumer = True
        user.save()
        Consumer.objects.create(user=user)
        return user

class MerchantUserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email')
        labels = { 'first_name' : 'Store Name'}

class MerchantDetailsEditForm(forms.ModelForm):
    class Meta:
        model = Merchant
        fields = ('address',)

class MerchantAddressEditForm(forms.ModelForm):
    #country = forms.ChoiceField(choices = COUNTRY_CHOICES)
    state = forms.ChoiceField(choices = STATE_CHOICES)
    class Meta:
        model = Merchant
        fields = ('state', 'city', 'zip_code')

class MerchantCardEditForm(forms.ModelForm):
    class Meta:
        model = Card_Details
        fields = ('account_number', 'expiry_data')
        #labels = { 'account_number' : 'Visa Card Number', 'expiry_data': 'Expiry Date'}
