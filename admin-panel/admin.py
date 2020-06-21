from django.contrib import admin

# Register your models here.
from .models import Consumer
from .models import Merchant
from .models import Offers
from .models import Orders

admin.site.register(Consumer)
admin.site.register(Merchant)
admin.site.register(Offers)
admin.site.register(Orders)