from django.db import models
from karmapoints.models import Orders

# Create your models here.
class Transactions(models.Model):
	order = models.OneToOneField(Orders, null=True, on_delete=models.SET_NULL)
	pull_transaction_identifier = models.IntegerField(null=True)
	push_transaction_identifier = models.IntegerField(null=True)
	pull_action_code = models.CharField(max_length=2, null=True)
	push_action_code = models.CharField(max_length=2, null=True)
	pull_approval_code = models.CharField(max_length=8, null=True)
	push_approval_code = models.CharField(max_length=8, null=True)
	pull_response_code = models.CharField(max_length=2, null=True)
	push_response_code = models.CharField(max_length=2, null=True)
	pull_status = models.CharField(max_length=300, null=True)
	push_status = models.CharField(max_length=300, null=True)
	pull_transmission_date_time = models.CharField(max_length=25, null=True)
	push_transmission_date_time = models.CharField(max_length=25, null=True)
	amount = models.DecimalField(decimal_places=2, max_digits=12, null=True)
	sender_card_id = models.CharField(max_length=19, null=True)
	recipient_card_id = models.CharField(max_length=19, null=True)
	txn_time = models.DateTimeField(auto_now_add=True, null=True)
	
	def __str__(self):
	    return str(self.id)