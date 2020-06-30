from django.urls import include, path

from .views import platform, consumer, merchant

urlpatterns = [
    path('', platform.home, name='home'),
    path('merchants/',merchant.Dashboard.as_view(), name='merchants_dashboard'),
    path('merchants/account',merchant.edit, name='merchants_account'),
    path('merchants/account/password', merchant.change_password, name='merrchants_change_password'),
    path('consumers/',consumer.Dashboard.as_view(), name='consumers_dashboard'),
]
