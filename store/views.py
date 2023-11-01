from django.shortcuts import render, get_object_or_404
from products.models import Product
from category.models import Category


def home(request, category_slug=None):
    """
    View for home page
    the function also displays url sorted category of products
    """

    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'index.html', context)
