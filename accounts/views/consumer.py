from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from django.db import transaction
from django.db.models import Count, Sum
from django.db.models.functions import Concat
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.views import View

from ..decorators import consumer_required
from ..forms import ConsumerSignUpForm

User = get_user_model()


@method_decorator([login_required, consumer_required], name='dispatch')
class Dashboard(TemplateView):
    template_name = 'accounts/consumers/dashboard.html'

class ConsumerSignUpView(CreateView):
    model = User
    form_class = ConsumerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'consumer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('consumers_dashboard')
