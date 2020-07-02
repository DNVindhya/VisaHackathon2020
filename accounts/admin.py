from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Consumer)
admin.site.register(Merchant)
admin.site.register(Card_Details)