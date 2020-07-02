from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Consumer)
# admin.site.register(Merchant)
admin.site.register(Offers)
admin.site.register(Orders)
admin.site.register(Tag)