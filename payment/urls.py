from django.urls import path
from . import views

urlpatterns = [
    #Leave as empty string for base url
	path('make_payment/', views.process_payment, name="make_payment"),
	path('success/',views.payment_success,name="payment_success"),
	path('failure/',views.payment_failure,name="paymnet_failure"),
]