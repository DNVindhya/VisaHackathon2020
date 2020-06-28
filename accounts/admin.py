from django.contrib import admin

# Register your models here.
from .models import User, Consumer, Merchant

admin.site.register(User)
admin.site.register(Consumer)
admin.site.register(Merchant)