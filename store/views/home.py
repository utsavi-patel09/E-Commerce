from django.shortcuts import render ,redirect
from store.models.product import Product
from store.models.category import Category
from django.views import View
class index(View):
    def get(selfself,request):
        product=None
        cart = request.session.get('cart')
        if not cart:
            request.session['cart']={}
        products = Product.get_all_products()
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')

        if categoryID:
            products = Product.get_all_product_by_id(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        print(request.session.get('email'))
        return render(request, 'index.html', data)

    def post(self,request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            #cart.clear()
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1

                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1

        else:
            cart={}
            cart[product] = 1
        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('homepage')


