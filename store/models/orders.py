from django.db import models
from .product import Product
from .customer import Customer
import datetime


# Create your models here.
class Orders(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    phone = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=200, default='')
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default='False')

    def placeorder(self):
        self.save()

    @staticmethod
    def get_all_order():
        return Orders.objects.all()
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Orders.objects.filter(customer=customer_id).order_by('-date')
