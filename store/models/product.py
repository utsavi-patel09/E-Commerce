from django.db import models
from .category import Category
from .customer import Customer

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50,default='')
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200,default='')
    image = models.ImageField(upload_to='products/',default='')


    def register(self):
        self.save()
    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in = ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_product_by_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()