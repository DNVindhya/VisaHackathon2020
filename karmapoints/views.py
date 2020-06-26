from django.shortcuts import render
from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.
def view_karma_points(request):
	user=request.user.consumer
	current_karma_points=user.current_karma_points
	orders=Orders.objects.filter(consumer=user).order_by('-order_date')
	order_json=list(orders.values())
	data={}
	data["current_karma_points"]=current_karma_points
	data["transactions"]=order_json
	return JsonResponse(data,safe=False);

def get_orders(request):
	user=request.user.merchant
	orders=Orders.objects.filter(merchant=user).order_by('-order_date')
	context = {'orders': orders}
	return context