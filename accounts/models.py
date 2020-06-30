from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django_countries.fields import CountryField
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
    card_details = models.IntegerField(null = True)
    date_created = models.DateTimeField(auto_now_add= True, null = True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16,null=True,blank=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16,null=True,blank=True) 

    def __str__(self):
        return self.user.username
