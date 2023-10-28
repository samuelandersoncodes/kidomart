from django.shortcuts import render
from products.models import Product


def home(request):
    """View for home page"""
    products = products.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }
    return render(request, 'index.html')
