from django.shortcuts import render ,redirect, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.contrib.auth.hashers import make_password,check_password
from store.models.Delivery import Delivery
from store.models.admin import Admin
from django.views import View
from store.models.orders import Orders

class Admin_login(View):

    return_url = None
    def get(self,request):
        Admin.return_url = request.GET.get('return_url')
        return render(request, 'AdminLogin.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Admin.get_person(email)
        error_message = None
        if customer:

            if password == customer.password:
                print("yes")
                request.session['customer'] = customer.id
                return redirect('admincontrol')

            else:
                error_message = "Email or Password invalid"
        else:
            error_message = "Email or Password invalid"
            return render(request, 'AdminLogin.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('homepage')

def pending(request):
    pending.return_url = request.GET.get('return_url')
    orders = Orders.get_all_order()
    return render(request, 'pending.html', {'orders': orders})

def completed(request):
    completed.return_url = request.GET.get('return_url')
    orders = Orders.get_all_order()
    return render(request, 'completed.html', {'orders': orders})