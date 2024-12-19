from django.shortcuts import render ,redirect, HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.contrib.auth.hashers import make_password,check_password
from store.models.Delivery import Delivery
from django.views import View
from store.models.orders import Orders

class delivery_login(View):

    return_url = None
    def get(self,request):
        delivery_login.return_url = request.GET.get('return_url')
        return render(request, 'delivery_login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Delivery.get_person(email)
        error_message = None
        if customer:

            if password==customer.password:
                print("yes")
                request.session['customer'] = customer.id
                return redirect('delivery_details')

            else:
                error_message = "Email or Password invalid"
        else:
            error_message = "Email or Password invalid"
            return render(request, 'delivery_login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('homepage')
