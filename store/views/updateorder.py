from django.views import View
from store.models.product import Product
from store.models.orders import Orders
from store.middlewares.auth import auth_middleware
from django.shortcuts import render ,redirect

class update_order_status(View):
    def get(self,request):
        return redirect("delivery_details")
    def post(self,request):
        order_id = request.POST.get("order_id")
        new_status = request.POST.get("status") == "True"  # Convert string to boolean

        # Fetch the order and update its status
        order = Orders.objects.get(id=order_id)
        order.status = new_status
        order.save()

        return redirect("delivery_details")  # Replace with your orders view name