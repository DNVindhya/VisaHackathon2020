from django.shortcuts import render
from django.shortcuts import render
from .models import *
from offers.models import *
from django.http import JsonResponse
import json
import requests
import time
from geopy.distance import geodesic

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

def earn_karma_points(request):
	print("checked")
	merchants=Merchant.objects.all()
	listofmerchants=[]
	for merchant in merchants:
		dictval={}
		print(merchant)
		print(merchant.id)
		dictval["merchant_id"] = merchant.id
		dictval["merchant_name"]=merchant.name
		dictval["address"]=merchant.address
		dictval["offers"]=list(Offers.objects.filter(merchant=merchant).values())
		listofmerchants.append(dictval)
	return JsonResponse(listofmerchants,safe=False);

def earn_offers(request, pk):
	offers = Offers.objects.filter(merchant = pk)
	merchant = list(Merchant.objects.filter(id = pk).values())
	print(merchant)
	context = {'offers': offers, 'merchant': merchant[0]['name'], 'merchant_address': merchant[0]['address']}
	return render(request,'consumers/cons_earn_offers.html',context)
	

def avail_karma_points(request):
	latitude=request.GET.get('lat');
	longitude=request.GET.get('lng');
	#user=request.user.consumer
	#user.curr_lat=latitude
	#user.curr_long=longitude
	#user.save()
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

	return JsonResponse(offer_list,safe=False);

def confirm_order(request):
	#print("confirm_order_view")
	offer_id=request.POST.get('offerId')
	order_amount=float(request.POST.get('order_amount'))
	#print(offer_id)
	offer=list(Offers.objects.filter(id=offer_id).values())[0]
	#print(offer['percentage_off'])
	#print(type(offer['percentage_off']))
	#print(type(order_amount))
	final_amount=order_amount-(order_amount*offer['percentage_off']/100)
	#final_amount=order_amount
	context={'order_amount':order_amount,'offer':offer,'final_amount':final_amount}
	return render(request,'consumers/cons_offer_profile.html',context)