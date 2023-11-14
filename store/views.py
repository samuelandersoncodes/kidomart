from django.shortcuts import render, get_object_or_404
from django.http import Http404
from products.models import Product
from category.models import Category


def home(request, category_slug=None):
    """
    View for home page
    the function also displays url sorted category of products,
    their respective category names and product counts
    """
    selected_category = None
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
        'selected_category': selected_category,
        'categories': categories,
    }
    return render(request, 'index.html', context)


def product_detail(request, category_slug, product_slug):
    # product detail view
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Product.DoesNotExist:
        raise Http404("Sorry! This product does not exist")
    
    context = {
        'single_product': single_product,
    }
    return render(request, 'product_detail.html', context)
