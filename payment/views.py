from __future__ import print_function
import time
from .funds_transfer_api.apis.funds_transfer_api import FundsTransferApi
from .funds_transfer_api.configuration import Configuration

import os
import sys
import unittest
import datetime
import pytz
import random
import string
import re
import json

from payment.forms import PaymentForm
from datetime import datetime, timedelta

from django.shortcuts import render, redirect
from offers.models import *
from karmapoints.models import *
from .models import *

# Create your views here.
def process_payment(request):


def payment_success(request):
	context = {}
	return render(request, 'payment/success.html', context)

def payment_failure(request):
	context = {}
	return render(request, 'payment/failure.html', context)




