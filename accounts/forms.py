from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from accounts.models import ( Consumer, Merchant, User)


class MerchantSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        #fields = ('username', 'first_name', 'last_name', 'email')

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
