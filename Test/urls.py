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
from django.urls import path
from django.conf import settings

from django.http import HttpResponse
from django.shortcuts import render

from django.conf.urls.static import static

def homepage(request):
    return render(request, 'index.html')
    # return HttpResponse('Home Page')

def login(request):
    return render(request, 'log_in.html')

def signup(request):
    return render(request, 'sign_up.html')

def custwallet(request):
    return render(request, 'wallet.html')

def custlogin(request):
    return HttpResponse('Login Page for Customer')

def merchlogin(request):
    return HttpResponse('Login Page for Merchant')

def custsignup(request):
    return HttpResponse('SignUp Page for Customer')

def merchsignup(request):
    return HttpResponse('SignUp Page for Merchant')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('index/', homepage),
    path('login/', login),
    path('signup/', signup),
    path('custlogin/', custlogin),
    path('custsignup/', custsignup),
    path('merchlogin/', merchlogin),
    path('merchsignup/', merchsignup),
    path('wallet/', custwallet),
    
]+ static(settings.STATIC_URL)


