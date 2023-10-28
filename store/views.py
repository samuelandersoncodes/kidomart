from django.shortcuts import render
from products.models import Product


def home(request):
    """View for home page"""
    product_items = Product.objects.all().filter(is_available=True)

    context = {
        'products': product_items,
    }
    
    return render(request, 'index.html', context)
    
