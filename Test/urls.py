"""Test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.http import HttpResponse
from django.shortcuts import render

from offers.views import get_offers
from karmapoints.views import get_orders

from accounts.views import platform, merchant, consumer
from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
from accounts.decorators import merchant_required


def homepage(request):
    return render(request, 'landing/index.html')
    # return HttpResponse('Home Page')

def login(request):
    return render(request, 'landing/log_in.html')

def signup(request):
    return render(request, 'landing/sign_up.html')

def custlogin(request):
    return HttpResponse('Login Page for Customer')

def merchlogin(request):
    return HttpResponse('Login Page for Merchant')

def custsignup(request):
    return HttpResponse('SignUp Page for Customer')

def merchsignup(request):
    return HttpResponse('SignUp Page for Merchant')

def consearn(request):
    return render(request, 'consumers/cons_earn.html')

def consavail(request):
    return render(request, 'consumers/cons_avail.html')

def conswallet(request):
    return render(request, 'consumers/cons_wallet.html')

def consorders(request):
    return render(request, 'consumers/cons_orders.html')

def consofferprofile(request):
    return render(request, 'consumers/cons_offer_profile.html')

def consearnpoints(request):
    return render(request, 'consumers/cons_earnpoints.html')

@login_required
@merchant_required
def merchdashboard(request):
    all_offers = get_offers(request)
    return render(request, 'merchants/merch_dashboard.html', all_offers)

@login_required
@merchant_required
def merchorders(request):
    all_orders = get_orders(request)
    return render(request, 'merchants/merch_orders.html', all_orders)

@login_required
@merchant_required
def merchreport(request):
    return render(request, 'merchants/merch_report.html')

@login_required
@merchant_required
def merchaccount(request):
    return render(request, 'merchants/merch_account.html')

def custwallet(request):
    return render(request, 'wallet.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/consumer/', consumer.ConsumerSignUpView.as_view(), name='consumer_signup'),
    path('accounts/signup/merchant/', merchant.MerchantSignUpView.as_view(), name='merchant_signup'),
    #path('index/', homepage),
    #path('login/', login),
    #path('signup/', signup),
    path('custlogin/', custlogin),
    path('custsignup/', custsignup),
    path('merchlogin/', merchlogin),
    path('merchsignup/', merchsignup),
    path('offers/',include('offers.urls')),
    path('customer/',include('karmapoints.urls')),
    path('merchdashboard/', merchdashboard, name='merchants_dashboard'),
    path('merchorders/', merchorders),
    path('merchreport/', merchreport),
    #path('merchaccount/', merchaccount, name='merchants_account'),
    path('consearn/', consearn),
    path('consavail/', consavail),
    path('conswallet/', conswallet),
    path('consorders/', consorders),
    path('consofferprofile/', consofferprofile),
    path('consearnpoints/', consearnpoints),
]


