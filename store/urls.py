from django.contrib import admin
from django.urls import path
from .views import home, signup, login
from .views.cart import Cart
from .views.checkout import Checkout
from .views.orders import OredrView
from .views.delivery_login import delivery_login
from .views.delivery_details import delivery_details
from .views.updateorder import update_order_status
from .views.AdminLogin import Admin_login,pending,completed
from .views.admincontrol import admincontrol,Products,category,remove_product,remove_category,deliveryperson,remove_person



urlpatterns = [
   path('',home.index.as_view(), name='homepage'),
   path('signup', signup.Signup.as_view(),name="signup"),
   path('login', login.Login.as_view(),name="login"),
   path('logout', login.logout,name="logout"),
path('cart',Cart.as_view() ,name="cart"),
path('check-out',Checkout.as_view() ,name="checkout"),
path('orders',OredrView.as_view() ,name="orders"),
path('delivery_login',delivery_login.as_view() ,name="delivery_login"),
path('delivery_details',delivery_details.as_view() ,name="delivery_details"),
path('updateorder',update_order_status.as_view() ,name="updateorder"),
path('AdminLogin',Admin_login.as_view() ,name="admin_login"),
path('admincontrol',admincontrol.as_view() ,name="admincontrol"),
path('product',Products.as_view() ,name="product"),
path('category',category.as_view() ,name="category"),
path('deliveryperson',deliveryperson.as_view() ,name="deliveryperson"),
path('removeproduct',remove_product.as_view() ,name="removeproduct"),
path('removecategory',remove_category.as_view() ,name="removecategory"),
path('removeperson',remove_person.as_view() ,name="removeperson"),
path('pending', pending,name="pending"),
path('completed', completed,name="completed"),
]