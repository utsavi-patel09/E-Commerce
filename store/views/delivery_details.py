from django.shortcuts import render ,redirect, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.contrib.auth.hashers import make_password,check_password
from store.models.Delivery import Delivery
from django.views import View
from store.models.orders import Orders

class delivery_details(View):

    return_url = None
    def get(self,request):
        delivery_details.return_url = request.GET.get('return_url')
        orders = Orders.get_all_order()
        return render(request, 'delivery_details.html', {'orders':orders})