from django.db import models
from django.conf import settings

# Create your models here.
class Merchant(models.Model):
	user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,blank=True)
	name = models.CharField(max_length = 200, null = True)
	annual_revenue = models.IntegerField(null = True)
	business_category = models.CharField(max_length = 200, null = True)
	email = models.EmailField(max_length = 200, null = True)
	password = models.CharField(max_length = 200, null = True)
	address = models.CharField(max_length = 200, null = True)
	card_details = models.IntegerField(null = True)
	date_created = models.DateTimeField(auto_now_add= True, null = True)


	def __str__(self):
	    return self.name

class Offers(models.Model):
	merchant = models.ForeignKey(Merchant,null = True, on_delete = models.CASCADE)
	offer_name = models.CharField(max_length = 200, null = True)
	karma_points_required = models.IntegerField(null = True)
	percentage_off = models.IntegerField(null = True)
	offer_start_date = models.DateField(auto_now_add= True, null = True)
	offer_end_date = models.DateField(null = True)
	days_valid = models.IntegerField(null = True)
	details = models.TextField(null = True)

	def __str__(self):
	    return str(self.id)


