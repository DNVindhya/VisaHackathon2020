from django.db import models

# Create your models here.

class Consumer(models.Model):
    first_name = models.CharField(max_length = 100, null = True)
    last_name = models.CharField(max_length = 100, null = True)
    contact_number = models.IntegerField(max_length = 11, null = True)
    email = models.EmailField(max_length = 100, null = True)
    password = models.CharField(max_length = 100, null = True)
    address = models.CharField(max_length = 200, null = True)
    current_karma_points = models.IntegerField(null = True)
    card_details = models.IntegerField(max_length = 16, null = True)
    date_created = models.DateTimeField(auto_now_add= True, null = True)

    def __str__(self):
        return self.first_name


class Merchant(models.Model):
    merchant_name = models.CharField(max_length = 200, null = True)
    annual_revenue = models.IntegerField(null = True)
    business_category = models.CharField(max_length = 200, null = True)
    email = models.EmailField(max_length = 200, null = True)
    password = models.CharField(max_length = 200, null = True)
    address = models.CharField(max_length = 200, null = True)
    card_details = models.IntegerField(null = True)
    date_created = models.DateTimeField(auto_now_add= True, null = True)


    def __str__(self):
        return self.merchant_name

class Tag(models.Model):
    name = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.name

class Orders(models.Model):
    consumer = models.ForeignKey(Consumer, null = True, on_delete= models.CASCADE)
    merchant = models.ForeignKey(Merchant, null = True, on_delete= models.CASCADE)
    order_amount = models.IntegerField(null = True)
    order_date = models.DateTimeField(auto_now_add= True, null = True)
    discount_amount = models.IntegerField(null = True)
    karma_points_earned = models.IntegerField(null = True)
    karma_points_used = models.IntegerField(null = True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.order_date.__str__()

class Offers(models.Model):
    merchant = models.ForeignKey(Merchant,null = True, on_delete = models.CASCADE)
    karma_points = models.IntegerField(null = True)
    percentage_off = models.IntegerField(null = True)
    offer_start_date = models.DateTimeField(auto_now_add= True, null = True)
    days_valid = models.IntegerField(null = True)

    def __str__(self):
        return self.offer_start_date.__str__()




