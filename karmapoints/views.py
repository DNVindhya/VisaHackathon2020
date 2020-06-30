from django.shortcuts import render
from django.shortcuts import render
from .models import Orders
from offers.models import *
from django.http import JsonResponse
import json
import requests
import time
from geopy.distance import geodesic
from accounts.decorators import consumer_required
from django.contrib.auth.decorators import login_required
from accounts.models import Card_Details,User,Consumer

# Create your views here.
@login_required
@consumer_required
def view_karma_points(request):
	user=request.user.consumer
	current_karma_points=user.current_karma_points
	orders=Orders.objects.filter(consumer=user).order_by('-order_date')
	order_json=list(orders.values())
	data={}
	data["current_karma_points"]=current_karma_points
	data["transactions"]=order_json
	return JsonResponse(data,safe=False);

@login_required
@consumer_required
def view_orders(request):
	user=request.user.user_consumer
	orders=Orders.objects.filter(consumer=user).order_by('-order_date')
	context = {'orders': orders}
	print(orders)
	return render(request,'consumers/cons_orders.html',context)


def get_orders(request):
	user=request.user.user_merchant
	orders = Orders.objects.filter(merchant=user).order_by('-order_date')
	context = {'orders': orders}
	return context

@login_required
@consumer_required
def view_offers(request):
	user=request.user.user_consumer
	context={'user':user}
	return render(request,'consumers/cons_avail.html',context)

@login_required
@consumer_required
def view_merchants(request):
	context={}
	return render(request,'consumers/cons_earnpoints.html',context)

@login_required
@consumer_required
def earn_karma_points(request):
	print("checked")
	user=request.user.user_consumer
	user_loc=(user.curr_lat,user.curr_long)
	merchants=Merchant.objects.filter(latitude__isnull=True)
	for merchant in merchants:
		address = merchant.address
		api_key = "AIzaSyCLKMTl60zVE9QesazTh0Mxr8UjVD7THs4"
		api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
		api_response_dict = api_response.json()
		if api_response_dict['status'] == 'OK':
			merch_latitude = api_response_dict['results'][0]['geometry']['location']['lat']
			merch_longitude = api_response_dict['results'][0]['geometry']['location']['lng']
			#print ("Latitude:", latitude)
			#print ("Longitude:", longitude)
			merchant.latitude=merch_latitude
			merchant.longitude=merch_longitude
			merchant.save()
	merchants=Merchant.objects.all()
	listofmerchants=[]
	for merchant in merchants:
		merch_loc=(merchant.latitude, merchant.longitude) 
		dictval={}
		print(merchant)
		#print(merchant.id)
		dictval["merchant_id"] = merchant.username
		dictval["merchant_name"]=merchant.first_name
		dictval["address"]=merchant.address
		if merchant.latitude is not None:
			dictval["distance"]=geodesic(user_loc, merch_loc).miles
		else:
			dictval["distance"]=100000
		dictval["offers"]=list(Offers.objects.filter(merchant=merchant).values())
		listofmerchants.append(dictval)
	print(listofmerchants)
	return JsonResponse(listofmerchants,safe=False);


@login_required
@consumer_required
def earn_offers(request, pk):
	offers = Offers.objects.filter(merchant = pk)
	user=request.user.user_consumer
	merchant = list(Merchant.objects.filter(id = pk).values())
	print(merchant)
	context = {'offers': offers, 'merchant': merchant[0]['name'], 'merchant_address': merchant[0]['address'],'user':user}
	return render(request,'consumers/cons_earn_offers.html',context)
	
@login_required
@consumer_required
def avail_karma_points(request):
	latitude=request.GET.get('lat');
	longitude=request.GET.get('lng');
	user=request.user.user_consumer
	user.curr_lat=latitude
	user.curr_long=longitude
	user.save()
	user_loc=(latitude,longitude)
	merchants=Merchant.objects.filter(latitude__isnull=True)
	for merchant in merchants:
		address = merchant.address
		api_key = "AIzaSyCLKMTl60zVE9QesazTh0Mxr8UjVD7THs4"
		api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
		api_response_dict = api_response.json()
		if api_response_dict['status'] == 'OK':
			merch_latitude = api_response_dict['results'][0]['geometry']['location']['lat']
			merch_longitude = api_response_dict['results'][0]['geometry']['location']['lng']
			#print ("Latitude:", latitude)
			#print ("Longitude:", longitude)
			merchant.latitude=merch_latitude
			merchant.longitude=merch_longitude
			merchant.save()
	merchants=Merchant.objects.all()
	listofmerchants=[]
	for merchant in merchants:
		merch_loc=(merchant.latitude, merchant.longitude) 
		dictval={}
		dictval["merchant"]=merchant.name
		if merchant.latitude is not None:
			dictval["distance"]=geodesic(user_loc, merch_loc).miles
		else:
			dictval["distance"]=100000
		dictval["offers"]=list(Offers.objects.filter(merchant=merchant).values())
		listofmerchants.append(dictval)
	data=sorted(listofmerchants, key=lambda x: x['distance'])
	#print(data)
	#print(latitude)
	#print(longitude)
	#data={}
	#data["latitude"]=latitude
	#data["longitude"]=longitude
	#offers=list(Offers.objects.all().values())
	offer_list=[]
	for val in data:
		offers=val["offers"]
		for offer in offers:
			offer["merchant_name"]=val["merchant"]
			offer["distance"]=val["distance"]
			offer_list.append(offer)
	#print(offer_list)

	return JsonResponse(offer_list,safe=False)

@login_required
@consumer_required
def confirm_order(request):
	user=request.user
	#print("confirm_order_view")
	offer_id=request.POST.get('offerId')
	order_amount=float(request.POST.get('order_amount'))
	# print(offer_id)
	offer1 = list(Offers.objects.filter(id=offer_id).values())[0]
	offer = Offers.objects.get(id = offer_id)
	print(offer1)
	merchant = Merchant.objects.get(id = offer1['merchant_id'])
	#print(offer['percentage_off'])
	#print(type(offer['percentage_off']))
	#print(type(order_amount))
	final_amount=order_amount-(order_amount*offer1['percentage_off']/100)
	card_details=Card_Details.objects.get(user=user)
	#final_amount=order_amount
	context={'order_amount':order_amount,'offer':offer,'final_amount':final_amount,'merchant':merchant,'user':user,'card_details':card_details}
	return render(request,'consumers/cons_offer_profile.html',context)

def process_payment(request):
	merchant_id=request.POST.get('merchant_id')
	consumer_id=request.POST.get('user_id')
	offer_id=request.POST.get('offer_id')
	card_id=request.POST.get('card_details_id')
	offer = Offers.objects.get(id = offer_id)
	card_details=Card_Details.objects.get(id=card_id)
	merchant=Merchant.objects.get(id=merchant_id)
	user=request.user.user_consumer
	print(merchant)
	print(offer)
	print(card_details)
	return JsonResponse('Payment Complete',safe=False);

def payment_success(request):
	context={}
	return render(request,'consumers/cons_payment_success.html',context)
