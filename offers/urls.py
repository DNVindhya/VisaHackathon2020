from django.urls import path
from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.merchant, name="merchant"),
	path('create_offers/', views.create_offers, name="create_offers"),
	path('view_offers/', views.view_offers, name="view_offers"),
	path('delete_offer/<str:pk>/', views.delete_offer, name="delete_offer"),
	path('update_offer/<str:pk>/', views.update_offer, name="update_offer"),

]