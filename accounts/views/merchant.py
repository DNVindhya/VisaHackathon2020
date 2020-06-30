from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, TemplateView)

from ..decorators import merchant_required
from ..forms import MerchantSignUpForm, MerchantUserEditForm, MerchantDetailsEditForm, MerchantAddressEditForm, MerchantCardEditForm

from ..models import Card_Details

User = get_user_model()

@method_decorator([login_required, merchant_required], name='dispatch')
class Dashboard(TemplateView):
    template_name = 'accounts/merchants/dashboard.html'

class MerchantSignUpView(CreateView):
    model = User
    form_class = MerchantSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'merchant'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect('merchants_dashboard')

@login_required
@merchant_required
def edit(request):
    if request.method == 'POST':
        user_form = MerchantUserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = MerchantDetailsEditForm(
                                    instance=request.user.user_merchant,
                                    data=request.POST)
        address_form = MerchantAddressEditForm(
                                    instance=request.user.user_merchant,
                                    data=request.POST)
        card_details, created = Card_Details.objects.get_or_create(user=request.user)
        card_form = MerchantCardEditForm(instance=card_details,
                                    data=request.POST)
        if user_form.is_valid() and profile_form.is_valid() and address_form.is_valid() and card_form.is_valid():
            user_form.save()
            #user = password_change.save()
            #update_session_auth_hash(request, user)  
            profile_form.save()
            address_form.save()
            card_form.save()
       
    else:
        user_form = MerchantUserEditForm(instance=request.user)
        profile_form = MerchantDetailsEditForm(
                                    instance=request.user.user_merchant)
        address_form = MerchantAddressEditForm(instance=request.user.user_merchant)
        password_change = PasswordChangeForm(request.user)
        card_detail, created = Card_Details.objects.get_or_create(user=request.user)
        card_form = MerchantCardEditForm(instance=card_detail)

    return render(request,
                  'merchants/merch_account.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'address_form': address_form,
                   'card_form':card_form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            #return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'merchants/merch_password.html', {
        'form': form
    })