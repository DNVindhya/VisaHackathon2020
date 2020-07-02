from django.db import models
from django.conf import settings
from accounts.models import Merchant

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


