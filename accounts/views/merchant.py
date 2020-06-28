from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, TemplateView)

from ..decorators import merchant_required
from ..forms import MerchantSignUpForm

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
