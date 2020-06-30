from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
import requests

COUNTRY_CHOICES =( 
    ("1", "USA") 
) 

STATE_CHOICES =( 
    ("1", "California") 
) 

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
    annual_revenue = models.IntegerField(null = True)
    business_category = models.CharField(max_length = 200, null = True)
    address = models.CharField(max_length = 200, null = True)
    city = models.CharField(max_length = 200, null = True)
    state = models.CharField(max_length = 200, null = True)
    #country = CountryField(multiple=False)
    #state = USStateField('state')
    zip_code = models.CharField('zip code',null= True, max_length=5)
    #card_details = CardNumberField('card number')
    #cc_expiry = CardExpiryField('expiration date')
    #cc_code = SecurityCodeField('security code')
    #card_details = models.IntegerField(null = True)
    date_created = models.DateTimeField(auto_now_add= True, null = True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16,null=True,blank=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16,null=True,blank=True) 

    def update_location(self):
        address = self.address+','+self.city+','+self.state+','+self.zip_code
        api_key = "AIzaSyCLKMTl60zVE9QesazTh0Mxr8UjVD7THs4"
        api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
        api_response_dict = api_response.json()
        print(api_response_dict)
        if api_response_dict['status'] == 'OK':
            self.latitude = api_response_dict['results'][0]['geometry']['location']['lat']
            self.longitude = api_response_dict['results'][0]['geometry']['location']['lng']
            print ("Latitude:", self.latitude)
            print ("Longitude:", self.longitude)
            
    def __str__(self):
        return self.user.username

class Card_Details(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	account_number=models.CharField(max_length=19)
	expiry_data=models.CharField(max_length=7)

	def __str__(self):
		return self.user.username   

