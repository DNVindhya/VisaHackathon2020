from django.shortcuts import render,redirect

# Create your views here.

from django.contrib.auth.models import User
from .models import *

# Create your views here.
def merchant(request):
	context = {}
	return render(request, 'offers/merchant.html', context)

def create_offers(request):
	context = {}
	return render(request, 'offers/create_offers.html', context)

def view_offers(request):
	user=request.user.merchant
	print(user.id)
	offers=Offers.objects.filter(merchant=user)
	print(offers)
	context = {'offers':offers}
	return render(request, 'offers/view_offers.html', context)

def delete_offer(request,pk):
	offer=Offers.objects.filter(id=pk)
	if request.method =="POST":
		offer.delete()
		return redirect('/offers/view_offers')
	context={'offer':offer, 'offerid':pk}
	return render(request,'offers/delete_offer.html',context)

def update_offer(request,pk):
	offer=Offers.objects.filter(id=pk)
	if request.method=="POST":
		return redirect('/offers/view_offers')
	return render(request,'offers/offer_form.html',context)

