
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,default='')


    def register(self):
        self.save()
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    @staticmethod
    def get_all_product_by_id(category_id):
        if category_id:
            return Category.objects.filter(category= category_id)
        else:
            return Category.objects.all()

    def __str__(self):
        return self.name

