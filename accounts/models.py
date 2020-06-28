from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


class User(AbstractUser):
    is_consumer = models.BooleanField(default=False)
    is_merchant = models.BooleanField(default=False)
    
    
class Consumer(models.Model):
    user = models.OneToOneField(User, related_name="user_consumer", on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Merchant(models.Model):
    user = models.OneToOneField(User, related_name="user_merchant", on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username
