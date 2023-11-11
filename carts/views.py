from django.shortcuts import render, redirect
from products.models import Product
from .models import Cart, CartItem


def _cart_id(request):
    """
    Helper function to get or create a unique cart ID for the current session 
    It checks if a cart ID is already present in the session
    If not, it creates a new session and use its key as the cart id
    """
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def cart(request):
    # View to display cart template
    return render(request, 'cart.html')
