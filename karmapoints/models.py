from django.db import models
from django.conf import settings
from accounts.models import User, Consumer
from offers.models import *

class Orders(models.Model):
	consumer = models.ForeignKey(Consumer, null = True, on_delete= models.SET_NULL)
	merchant = models.ForeignKey(Merchant, null = True, on_delete= models.SET_NULL)
	offer = models.ForeignKey(Offers, null=True, on_delete=models.SET_NULL)
	order_amount = models.DecimalField(null = True, max_digits=12, decimal_places=2)
	order_date = models.DateTimeField(auto_now_add= True, null = True)
	discount_amount = models.DecimalField(null = True, max_digits=12, decimal_places=2)
	karma_points_earned = models.IntegerField(null = True)
	karma_points_used = models.IntegerField(null = True)

	def __str__(self):
	    return str(self.id)
	    

