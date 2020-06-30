from django.db import models
from django.conf import settings
from accounts.models import User, Consumer
from offers.models import *

# Create your models here.
# class Consumer(models.Model):
# 	user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,blank=True)
# 	first_name = models.CharField(max_length = 100, null = True)
# 	last_name = models.CharField(max_length = 100, null = True)
# 	contact_number = models.IntegerField(null = True)
# 	email = models.EmailField(max_length = 100, null = True)
# 	password = models.CharField(max_length = 100, null = True)
# 	address = models.CharField(max_length = 200, null = True)
# 	current_karma_points = models.IntegerField(null = True)
# 	card_details = models.IntegerField(null = True)
# 	date_created = models.DateTimeField(auto_now_add= True, null = True)
# 	curr_lat = models.DecimalField(max_digits=22, decimal_places=16,null=True,blank=True)
# 	curr_long = models.DecimalField(max_digits=22, decimal_places=16,null=True,blank=True)

# 	def __str__(self):
# 	    return self.first_name

class Orders(models.Model):
	consumer = models.ForeignKey(Consumer, null = True, on_delete= models.SET_NULL)
	merchant = models.ForeignKey(Merchant, null = True, on_delete= models.SET_NULL)
	offer = models.ForeignKey(Offers, null=True, on_delete=models.SET_NULL)
	order_amount = models.IntegerField(null = True)
	order_date = models.DateTimeField(auto_now_add= True, null = True)
	discount_amount = models.IntegerField(null = True)
	karma_points_earned = models.IntegerField(null = True)
	karma_points_used = models.IntegerField(null = True)

	def __str__(self):
	    return str(self.id)
	    

