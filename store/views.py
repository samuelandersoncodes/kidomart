from django.shortcuts import render, get_object_or_404
from django.http import Http404
from products.models import Product
from category.models import Category
from carts.views import _cart_id
from carts.models import CartItem
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def home(request, category_slug=None):
    """
    View for home page
    the function also displays url sorted category of products,
    their respective category names and product counts
    Various pages are also paginated
    """
    selected_category = None
    products = None

    if category_slug != None:
        selected_category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=selected_category, is_available=True)
        paginator = Paginator(products, 8)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('-id')
        paginator = Paginator(products, 12)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    context = {
        'products': paged_products,
        'product_count': product_count,
        'selected_category': selected_category,
    }
    return render(request, 'index.html', context)


def product_detail(request, category_slug, product_slug):
    # product detail view
    try:
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(
            request), product=single_product).exists()
    except Product.DoesNotExist:
        raise Http404("Sorry! This product does not exist")

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'product_detail.html', context)
