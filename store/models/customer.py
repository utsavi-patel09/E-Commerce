from django.db import models


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=15, default='')
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def get_customer(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isexists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False