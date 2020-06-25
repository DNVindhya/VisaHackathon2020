from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('karma_points/', views.view_karma_points, name="karma_points"),

]