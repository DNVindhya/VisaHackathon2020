from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from offers.forms import CreateUpdateOfferForm
from datetime import datetime, timedelta
from .models import *

# Create your views here.
def merchant(request):
	context = {}
	return render(request, 'offers/merchant.html', context)

def create_update_offer(request, pk=None):
	# Instantiating offer object
	if pk:
		offer = Offers.objects.get(id=pk)
	else:
		offer = Offers()

	# Create a form instance and poulate it with data from the request (binding)
	form = CreateUpdateOfferForm(request.POST or None)

	# If this is a POST request then process the Form data
	if request.method == 'POST':
		# Check if the form is valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			offer.offer_name = form.cleaned_data['offer_name']
			offer.karma_points_required = form.cleaned_data['karma_points']
			offer.percentage_off = form.cleaned_data['percent_off']
			offer.offer_start_date = form.cleaned_data['start_date']
			offer.days_valid = form.cleaned_data['validity']
			offer.details = form.cleaned_data['details']

			# Calculating last day of offer
			last_day  = offer.offer_start_date + timedelta(days=offer.days_valid)
			offer.offer_end_date = last_day

			# Merchant creating the offer
			offer.merchant = request.user.merchant
			offer.save()

			# redirect to show newly created offer
			return redirect('/offers/view_offers')
	# If this is a GET (or any other method) create the default form and populate values (only for an update)
	else:
		# Get offer details for id passed for updating
		if pk:
			existing_offer_name = offer.offer_name
			existing_karma_points = offer.karma_points_required
			existing_percent_off =  offer.percentage_off
			existing_start_date = offer.offer_start_date
			existing_validity = offer.days_valid
			existing_details = offer.details
			# Create a form instance with above values
			form = CreateUpdateOfferForm(initial={'offer_name':existing_offer_name,'karma_points':existing_karma_points,
			    'percent_off':existing_percent_off,'start_date':existing_start_date,'validity':existing_validity,
			    'details':existing_details})
	context = {
		'form': form
	}
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