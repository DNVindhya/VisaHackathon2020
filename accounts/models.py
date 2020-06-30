from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


class User(AbstractUser):
    is_consumer = models.BooleanField(default=False)
    is_merchant = models.BooleanField(default=False)
    
    
class Consumer(models.Model):
	user = models.OneToOneField(User, related_name="user_consumer", on_delete=models.CASCADE, primary_key=True)
	contact_number = models.IntegerField(null=True)
	address = models.CharField(max_length = 200, null = True, blank=True)
	current_karma_points = models.IntegerField(null = True, blank=True)
	date_created = models.DateTimeField(auto_now_add= True, null = True)
	curr_lat = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
	curr_long = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)

	def __str__(self):
		return self.user.username


class Merchant(models.Model):
    user = models.OneToOneField(User, related_name="user_merchant", on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

class Card_Details(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	account_number=models.CharField(max_length=19)
	expiry_data=models.CharField(max_length=7)

	def __str__(self):
		return str(self.id)

