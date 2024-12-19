from django.shortcuts import render ,redirect, HttpResponseRedirect, get_object_or_404
from store.models.product import Product
from store.models.category import Category
from django.contrib.auth.hashers import make_password,check_password
from store.models.Delivery import Delivery
from django.views import View
from store.models.orders import Orders

class admincontrol(View):

    return_url = None
    def get(self,request):
        admincontrol.return_url = request.GET.get('return_url')
        products = Product.get_all_products()
        categorys= Category.get_all_categories()
        return render(request, 'admincontrol.html', {'products':products, 'categories':categorys})

class Products(View):

    return_url = None
    def get(self,request):
        Products.return_url = request.GET.get('return_url')
        products = Product.get_all_products()
        categorys = Category.get_all_categories()
        return render(request, 'product.html', {'products':products,'categories':categorys})

    def post(self, request):
        postData = request.POST
        product_name = postData.get('productname')
        price = postData.get('price')
        category_id = postData.get('category')
        description = postData.get('description')
        image = request.FILES.get('image')

        # Capture form values in case of errors
        value = {
            'product_name': product_name,
            'price': price,
            'category': category_id,
            'description': description,
        }

        error_message = None

        # Fetch category from the database
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            error_message = "Invalid category selected."

        # Form validation
        if not product_name:
            error_message = "Product name is required."
        elif not price or not price.isdigit():
            error_message = "Valid price is required."
        elif not image:
            error_message = "Product image is required."

        categories = Category.get_all_categories()
        # If no errors, save the product
        if not error_message:
            product = Product(
                name=product_name,
                price=price,
                category=category,
                description=description,
                image=image,
            )
            product.register()
            products = Product.get_all_products()
            return render(request, 'product.html', {'products': products,'categories':categories})



        data = {
            'error': error_message,
            'values': value,
            'categories': categories,
        }
        products = Product.get_all_products()
        return render(request, 'product.html', {'products': products,'categories':categories})





class category(View):

    return_url = None
    def get(self,request):
        category.return_url = request.GET.get('return_url')
        categorys= Category.get_all_categories()
        return render(request, 'category.html', {'categories':categorys})

    def post(self, request):

        postData = request.POST
        category_name = postData.get('categoryname')


        value = {'first_name': category_name
                 }
        error_message = None

        category = Category(name=category_name)

        category.register()
        categorys = Category.get_all_categories()
        return render(request, 'category.html', {'categories': categorys})


def validatecustomer(customer):
    error_message=None
    if (not customer.first_name):
        error_message = "frist name required"
    elif len(customer.first_name) < 4:
        error_message = "First_name must be greater than 4 character"
    elif customer.isexists():
        error_message = "Email Address Already Registered"

    return error_message
class deliveryperson(View):

    return_url = None
    def get(self,request):
        person = Delivery.get_all()
        return render(request, 'deliveryperson.html', {'persons': person})

    def post(self, request):

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

        customer = Delivery(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            password=password,
                            phone=phone)

        error_message = validatecustomer(customer)

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('deliveryperson')

        else:
            data = {
                'error': error_message,
                'values': value
            }
        person = Delivery.get_all()
        return render(request, 'deliveryperson.html', {'persons': person})


class remove_product(View):
    def post(self,request):
        product_id = request.POST.get('remove_product_id')
        try:
            product = get_object_or_404(Product, id=product_id)
            product.delete()
        except Product.DoesNotExist:
            pass
        products = Product.get_all_products()
        categories = Category.get_all_categories()
        return render(request, 'product.html', {'products': products, 'categories': categories})


class remove_category(View):
    def post(self,request):
        category_id = request.POST.get('remove_category_id')
        try:
            category = get_object_or_404(Category, id=category_id)
            category.delete()
        except category.DoesNotExist:
            pass
        products = Product.get_all_products()
        categories = Category.get_all_categories()
        return render(request, 'category.html', {'products': products, 'categories': categories})

class remove_person(View):
    def post(self,request):
        person_id = request.POST.get('remove_person_id')
        try:
            person = get_object_or_404(Delivery, id=person_id)
            person.delete()
        except person.DoesNotExist:
            pass
        personss = Delivery.get_all()
        return render(request, 'deliveryperson.html', {'persons': personss})