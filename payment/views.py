from .visa_direct.apis.funds_transfer_api import FundsTransferApi
from .visa_direct.configuration import Configuration

from django.http import JsonResponse
from django.shortcuts import render, redirect
from accounts.models import Card_Details,User,Consumer,Merchant
from offers.models import Offers
from karmapoints.models import Orders
from .models import *
from .utils import action_code_to_txn_status

import datetime
import pytz
import random
import string
import re
import json
import os

def process_payment(request):

	# Authentication for VISA Direct APIs, replace with your credentials
	config = Configuration()
	module_dir = os.path.dirname(_file_) # get current directory
	config.username = '7SG6JCVBQX19D3ZTE9DX21Wd2mK1qDfxz6f65yFcCraHniopc'
	config.password = 'k3BVYK02PpAm27D82xwPf6dUkpmA2T282YYf8c'
	config.cert_file = os.path.join(module_dir,'cert.pem')
	config.key_file = os.path.join(module_dir,'key_4212dd3b-5b2a-4e00-b50d-4f227d4412af.pem')
	config.ssl_ca_cert = os.path.join(module_dir,'DigiCertGlobalRootCA.pem')

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

	api_instance = FundsTransferApi()

	pull_response = api_instance.postpullfunds(pullFundsRequestData)


	# Creating Request payload for PushFundsTransaction POST
	pushFundsRequestData = {}

	push_timestamp = timezone.localize(datetime.datetime.now()).strftime('%Y-%m-%dT%H:%M:%S')
	push_systemsTraceAuditNumber = ''.join(random.choice(string.digits) for _ in range(6))
	push_retrievalReferenceNumber = str(pull_timestamp[3]) + str(dayOfYear) + str(push_timestamp[-8:-6]) + str(push_systemsTraceAuditNumber)

	pullTransactionIdentifier = pull_response.transaction_identifier
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

	txn = Transactions()
	txn.pull_transaction_identifier   = pull_response.transaction_identifier
	txn.pull_action_code              = pull_response.action_code
	txn.pull_approval_code            = pull_response.approval_code
	txn.pull_response_code            = pull_response.response_code
	txn.pull_transmission_date_time   = pull_response.transmission_date_time
	txn.amount                        = amount
	txn.sender_card_id                = senderCardPAN


	pull_success = False
	push_success = False
	txn.pull_status = action_code_to_txn_status(txn.pull_action_code)
	print(txn.pull_status)

	if pull_response.action_code == "00":
		pull_success = True
		# Call Push Funds only when pull funds txn is approved 
		push_response = api_instance.postpushfunds(pushFundsRequestData)
		
		txn.push_transaction_identifier   = push_response.transaction_identifier
		txn.push_action_code              = push_response.action_code
		txn.push_approval_code            = push_response.approval_code
		txn.push_response_code            = push_response.response_code
		txn.push_transmission_date_time   = push_response.transmission_date_time
		txn.sender_card_id                = merchantCardPAN

		if push_response.action_code == "00":
			cur_order = Orders()
			cur_order.consumer = consumerDetails
			cur_order.merchant = merchantDetails
			cur_order.offer    = offerDetails
			cur_order.order_amount = float(ord_amount)
			cur_order.discount_amount = float(amount)
			cur_order.karma_points_used = offerDetails.karma_points_required
			cur_order.karma_points_earned = round((0.05) * float(amount))
			consumerDetails.current_karma_points = consumerDetails.current_karma_points - cur_order.karma_points_used + cur_order.karma_points_earned
			cur_order.save()
			consumerDetails.save()
			saved_order = Orders.objects.get(id=cur_order.id)
			txn.order = saved_order
			push_success = True

		txn.push_status = action_code_to_txn_status(txn.push_action_code)
		txn.save()

	message = {}
	if pull_success and push_success:
		print("Success")
		message['status'] = "SUCCESS"
		message['action_code'] = txn.push_status
		message['txn_id'] = txn.pull_transaction_identifier
		return JsonResponse(message,safe=False)
	else:
		print("Failure")
		message['status'] = "FAILURE"
		if pull_response.action_code != "00":
			message['action_code'] = txn.pull_status
		else:
			message['action_code'] = txn.push_status
		return JsonResponse(message,safe=False)
