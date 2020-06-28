from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('karma_points/', views.view_karma_points, name="karma_points"),
	path('avail_karma_points/',views.avail_karma_points,name="avail_karma_points"),
	path('earn_karma_points/',views.earn_karma_points,name="earn_karma_points")

]