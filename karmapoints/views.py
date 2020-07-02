from django.shortcuts import render, redirect, reverse
from .models import Orders
from offers.models import *
from django.http import JsonResponse
import json
import requests
import time
from geopy.distance import geodesic
from accounts.decorators import consumer_required
from django.contrib.auth.decorators import login_required
from accounts.models import Card_Details,User,Consumer, Merchant
from karmapoints.forms import ConsumerUserEditForm, ConsumerDetailsEditForm, ConsumerCardEditForm
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

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
	return JsonResponse(data,safe=False)

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

def get_orders_json(request):
	user=request.user.user_merchant
	orders = Orders.objects.filter(merchant=user).order_by('-order_date')
	orders_json = list(orders.values())
	data = {}
	data["orders"] = orders_json
	return JsonResponse(data, safe = False)

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
def wallet(request):
	context={}
	return render(request,'consumers/cons_wallet.html',context)

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
		dictval["merchant_id"] = merchant.user_id
		dictval["merchant_name"]=merchant.user.first_name
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
	#merchant = list(Merchant.objects.filter(user_id = pk).values())
	#print(merchant)
	merchant=Merchant.objects.get(user_id = pk)
	#context = {'offers': offers, 'merchant': merchant[0]['name'], 'merchant_address': merchant[0]['address'],'user':user,'merchant_obj':merchant_obj}
	context = {'offers': offers,'user':user,'merchant':merchant}
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
		dictval["merchant"]=merchant.user.first_name
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
	
	if request.POST.get('offerId'):
		#print("confirm_order_view")
		offer_id=request.POST.get('offerId')
		order_amount=request.POST.get('order_amount')
		if offer_id == None and order_amount == None:
			offer_id = request.session['offerId']
			order_amount = request.session['order_amount']

			if offer_id is not None and order_amount is not None:
				del request.session['order_amount']
				del request.session['offerId']
		order_amount = float(order_amount)
		# print(offer_id)
		offer1 = list(Offers.objects.filter(id=offer_id).values())[0]
		offer = Offers.objects.get(id = offer_id)
		print(offer1)
		merchant = Merchant.objects.get(user_id = offer1['merchant_id'])
		final_amount=order_amount-(order_amount*offer1['percentage_off']/100)
		discount_off = (order_amount*offer1['percentage_off']/100)
		percentage_off = offer.percentage_off
		karma_used = offer.karma_points_required

	else:
		order_amount=float(request.POST.get('order_amount'))
		merchant_id=request.POST.get('merchantId')
		merchant = Merchant.objects.get(user_id = merchant_id)
		offer = "False"
		final_amount = order_amount
		percentage_off = 0
		karma_used = 0
		discount_off = 0

	#print(offer['percentage_off'])
	#print(type(offer['percentage_off']))
	#print(type(order_amount))
	karma_earned = final_amount * 0.35
	try:
		card_details=Card_Details.objects.get(user=user)
	except:
		card_details=None
	#final_amount=order_amount
	if card_details == None or card_details.account_number == '':
		#response  = edit(request,{ 'offerId': offer_id, 'order_amount':order_amount })
		#return response
		request.session['offerId'] = offer_id
		request.session['order_amount'] = order_amount
		return redirect( reverse('consumers_account'), { 'offerId': offer_id, 'order_amount':order_amount })
	context={'order_amount':order_amount,'offer':offer,'final_amount':final_amount,'merchant':merchant,'user':user,'card_details':card_details, 'discount_off':discount_off, 'karma_earned': karma_earned, 'percentage_off': percentage_off, 'karma_used': karma_used}
	return render(request,'consumers/cons_offer_profile.html',context)

@login_required
@consumer_required
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

@login_required
@consumer_required
def payment_success(request):
	orderid=request.POST.get('order')
	order=Orders.objects.get(id=orderid)
	merchant=Merchant.objects.get(user_id=order.merchant)
	context={'order':order,'merchant':merchant.user.first_name}
	return render(request,'consumers/cons_payment_success.html',context)

@login_required
@consumer_required
def edit(request):
    if request.method == 'POST':
        user_form = ConsumerUserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ConsumerDetailsEditForm(
                                    instance=request.user.user_consumer,
                                    data=request.POST)
        card_details, created = Card_Details.objects.get_or_create(user=request.user)
        card_form = ConsumerCardEditForm(instance=card_details,
                                    data=request.POST)
        if user_form.is_valid() and profile_form.is_valid() and card_form.is_valid():
            user_form.save()
            #user = password_change.save()
            #update_session_auth_hash(request, user)  
            profile_form.save()
            card_form.save()
            # request.user.user_merchant.update_location()
            # request.user.user_merchant.save()
        try:	
            offer_id = request.session['offerId']
            order_amount = request.session['order_amount']
        except:
            offer_id = None
            order_amount = None

        if offer_id is not None and order_amount is not None:
            #del request.session['order_amount']
            #del request.session['offerId']
            return redirect(reverse('confirm_order'))

    else:
        try:	
            offer_id = request.session['offerId']
            order_amount = request.session['order_amount']
        except:
            offer_id = None
            order_amount = None

        if offer_id is not None and order_amount is not None:
            messages.add_message(request, messages.INFO, 'Please fill in the Account details below first')
			
        user_form = ConsumerUserEditForm(instance=request.user)
        profile_form = ConsumerDetailsEditForm(
                                    instance=request.user.user_consumer)
        card_detail, created = Card_Details.objects.get_or_create(user=request.user)
        card_form = ConsumerCardEditForm(instance=card_detail)

    return render(request,
                  'consumers/cons_account.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'card_form':card_form})

@login_required
@consumer_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            #return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'consumers/cons_password.html', {
        'form': form
    })