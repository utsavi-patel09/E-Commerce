from django.shortcuts import render ,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View

def validatecustomer(customer):
    error_message=None
    if (not customer.first_name):
        error_message = "frist name required"
    elif len(customer.first_name) < 4:
        error_message = "First_name must be greater than 4 character"
    elif customer.isexists():
        error_message = "Email Address Already Registered"

    return error_message


class Signup(View):
    def get(self,request):
        return render(request, 'signup.html')
    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        email = postData.get('email')
        password = postData.get('password')
        phone = postData.get('phone')

        value = {'first_name': first_name,
                 'last_name': last_name,
                 'email': email,
                 'phone': phone,
                 }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            password=password,
                            phone=phone)

        error_message = validatecustomer(customer)

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')

        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)




