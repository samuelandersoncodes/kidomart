from django.shortcuts import render, redirect
from carts. models import CartItem
from .forms import OrderForm
from .models import Order
import datetime

def place_order(request, total=0, quantity=0):
    # place order view
    current_user = request.user
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('cart')
    grand_total = 0
    tax = 0
    for cart_item in cart_items:
        if cart_item.product.on_sale:
            total += (cart_item.product.sale_price * cart_item.quantity)
        else:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
    tax = (1 * total)/100
    grand_total = total + tax
        else:
            return redirect('checkout')
    return redirect('checkout')
