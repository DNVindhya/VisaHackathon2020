from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('karma_points/', views.view_karma_points, name="karma_points"),
	path('avail_karma_points/',views.avail_karma_points,name="avail_karma_points"),
	path('earn_karma_points/',views.earn_karma_points,name="earn_karma_points"),
	path('earn_offers/<str:pk>/', views.earn_offers, name="earn_offers"),
	path('confirm_order/', views.confirm_order, name="confirm_order"),
	path('view_orders/',views.view_orders,name="view_orders"),
	path('',views.view_offers,name="view_offers"),
	path('view_merchants/',views.view_merchants,name="view_merchants"),
	path('process_payment/',views.process_payment,name="process_payment"),
	path('payment_success/',views.payment_success,name="payment_success"),
	path('pay_and_earn/',views.pay_and_earn,name="pay_and_earn"),
	path('wallet/',views.wallet,name="wallet"),
	path('account/',views.edit, name="consumers_account"),
	path('password/', views.change_password, name="customer_change_password")

]