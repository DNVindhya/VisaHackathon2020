from django.urls import path
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.merchant, name="merchant"),
	path('create_offer/', views.create_update_offer, name="create_offer"),
	path('delete_offer/<str:pk>/', views.delete_offer, name="delete_offer"),
	path('update_offer/<str:pk>/', views.create_update_offer, name="update_offer"),

]