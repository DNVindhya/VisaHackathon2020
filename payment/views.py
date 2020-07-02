from .visa_direct.apis.funds_transfer_api import FundsTransferApi
from .visa_direct.configuration import Configuration

from django.http import JsonResponse
from django.shortcuts import render, redirect
from accounts.models import Card_Details,User,Consumer,Merchant
from offers.models import Offers
from karmapoints.models import Orders
from .models import *

import datetime
import pytz
import random
import string
import re
import json

# Create your views here.
def process_payment(request):

	# Authentication for VISA Direct APIs, replace with your credentials
	config = Configuration()
	config.username = '7SG6JCVBQX19D3ZTE9DX21Wd2mK1qDfxz6f65yFcCraHniopc'
	config.password = 'k3BVYK02PpAm27D82xwPf6dUkpmA2T282YYf8c'
	config.cert_file = '/Users/yeti/Downloads/cert/cert.pem'
	config.key_file = '/Users/yeti/Downloads/cert/key_4212dd3b-5b2a-4e00-b50d-4f227d4412af.pem'
	config.ssl_ca_cert = '/Users/yeti/Downloads/cert/DigiCertGlobalRootCA.pem'	

	# Data available to Originator in Funds Transfer
	acquirerCountryCode = "840"
	acquiringBin        = "408999"
	businessApplicationId  = "AA"
	currencyCode           = "USD"
	settlementServiceIndicator = "9"
	cardAcceptor = {}
	cardAcceptor['address']    = {}
	cardAcceptor['address']['country'] = "USA"
	cardAcceptor['address']['county']  = "081"
	cardAcceptor['address']['state']   = "CA"
	cardAcceptor['address']['zipCode'] = "94404"
	cardAcceptor['idCode']     = "CA-IDCode-66565"
	cardAcceptor['name']       = "Acceptor 9"
	cardAcceptor['terminalId'] = "TID-1616"
	addressVerificationData               = {}
	addressVerificationData['street']     = "XYZ St"
	addressVerificationData['postalCode'] = "12345"
	timezone = pytz.timezone("America/Los_Angeles")
	dayOfYear = datetime.datetime.now().timetuple().tm_yday

	# Getting context data from confirm_order page
	merchantId = request.POST.get('merchant_id')
	consumerId = request.POST.get('user_id')
	cardId     = request.POST.get('card_details_id')
	offerId    = request.POST.get('offer_id')
	amount     = request.POST.get('final_amount')
	ord_amount = request.POST.get('order_amount')

	cardDetails     = Card_Details.objects.get(id=cardId)
	merchantDetails = Merchant.objects.get(user_id=merchantId)
	consumerDetails = Consumer.objects.get(user_id=consumerId)
	offerDetails    = Offers.objects.get(id=offerId)

	
	# Creating Request payload for PullFundsTransaction POST
	pullFundsRequestData = {}

	pull_timestamp = timezone.localize(datetime.datetime.now()).strftime('%Y-%m-%dT%H:%M:%S')
	pull_systemsTraceAuditNumber = ''.join(random.choice(string.digits) for _ in range(6))
	pull_retrievalReferenceNumber = str(pull_timestamp[3]) + str(dayOfYear) + str(pull_timestamp[-8:-6]) + str(pull_systemsTraceAuditNumber)

	senderCardPAN = cardDetails.account_number
	senderCardExp = cardDetails.expiry_data

	pullFundsRequestData['acquirerCountryCode'] = acquirerCountryCode
	pullFundsRequestData['acquiringBin'] = acquiringBin
	pullFundsRequestData['amount'] = amount
	pullFundsRequestData['businessApplicationId'] = businessApplicationId
	pullFundsRequestData['cardAcceptor'] = cardAcceptor
	pullFundsRequestData['localTransactionDateTime'] = pull_timestamp
	pullFundsRequestData['retrievalReferenceNumber'] = pull_retrievalReferenceNumber
	pullFundsRequestData['senderCardExpiryDate'] = senderCardExp	
	pullFundsRequestData['senderCurrencyCode'] = str(currencyCode)
	pullFundsRequestData['senderPrimaryAccountNumber'] = senderCardPAN
	pullFundsRequestData['systemsTraceAuditNumber'] = pull_systemsTraceAuditNumber
	pullFundsRequestData['addressVerificationData'] = addressVerificationData
	pullFundsRequestData['settlementServiceIndicator'] = settlementServiceIndicator

	print("PullFUnds Request JSON")
	print(pullFundsRequestData)

	api_instance = FundsTransferApi()

	api_response = api_instance.postpullfunds(pullFundsRequestData)
	print("POST PullFunds http response :")
	print(api_response)


	# Creating Request payload for PushFundsTransaction POST
	pushFundsRequestData = {}

	push_timestamp = timezone.localize(datetime.datetime.now()).strftime('%Y-%m-%dT%H:%M:%S')
	push_systemsTraceAuditNumber = ''.join(random.choice(string.digits) for _ in range(6))
	push_retrievalReferenceNumber = str(pull_timestamp[3]) + str(dayOfYear) + str(push_timestamp[-8:-6]) + str(push_systemsTraceAuditNumber)

	pullTransactionIdentifier = api_response.transaction_identifier
	merchantCard = Card_Details.objects.get(user=merchantId)
	merchantCardPAN = merchantCard.account_number

	pushFundsRequestData['systemsTraceAuditNumber'] = push_systemsTraceAuditNumber
	pushFundsRequestData['retrievalReferenceNumber'] = push_retrievalReferenceNumber
	pushFundsRequestData['localTransactionDateTime'] = push_timestamp
	pushFundsRequestData['acquiringBin'] = acquiringBin
	pushFundsRequestData['acquirerCountryCode'] = acquirerCountryCode
	pushFundsRequestData['senderAccountNumber'] = senderCardPAN
	pushFundsRequestData['transactionCurrencyCode'] = str(currencyCode)
	pushFundsRequestData['recipientPrimaryAccountNumber'] = str(merchantCardPAN)
	pushFundsRequestData['amount'] = amount
	pushFundsRequestData['businessApplicationId'] = businessApplicationId
	pushFundsRequestData['transactionIdentifier'] = str(pullTransactionIdentifier)
	pushFundsRequestData['cardAcceptor'] = cardAcceptor

	print("PushFUnds Request JSON")
	print(pushFundsRequestData)	
	print(json.dumps(pushFundsRequestData))

	api_response = api_instance.postpushfunds(pushFundsRequestData)
	print("POST PushFunds http response :")
	print(api_response)

	cur_order = Orders()
 
	if (api_response.action_code == "00"):
		print("Success")
		cur_order.consumer = consumerDetails
		cur_order.merchant = merchantDetails
		cur_order.offer    = offerDetails
		cur_order.order_amount = round(float(ord_amount))
		cur_order.discount_amount = round(float(amount))
		cur_order.karma_points_used = offerDetails.karma_points_required
		cur_order.karma_points_earned = round((0.35) * float(amount))
		print(cur_order.karma_points_earned)
		print(cur_order)
		consumerDetails.current_karma_points = consumerDetails.current_karma_points - cur_order.karma_points_used + cur_order.karma_points_earned
		cur_order.save()
		consumerDetails.save()
		return JsonResponse('Payment Complete',safe=False);
	else:
		print("Failure")
		return JsonResponse('Payment Failure',safe=False);

	# return JsonResponse('Payment Complete',safe=False)

def payment_success(self, request):
	context = {}
	return render(request, 'payment/success.html', context)

def payment_failure(self, request):
	context = {}
	return render(request, 'payment/failure.html', context)
