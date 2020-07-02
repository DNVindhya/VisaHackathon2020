from django.urls import path
from . import views

urlpatterns = [
    #Leave as empty string for base url
	path('process_payment/', views.process_payment, name="process_payment"),
]