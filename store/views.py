from django.shortcuts import render, get_object_or_404
from django.http import Http404
from products.models import Product
from orders.models import OrderProduct
from category.models import Category
from carts.views import _cart_id
from carts.models import CartItem
from products.models import ReviewRating
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q


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
    orderproduct = None
    if request.user.is_authenticated:
        try:
            orderproduct = OrderProduct.objects.filter(
                user=request.user, product_id=single_product.id)
        except OrderProduct.DoesNotExist:
            orderproduct = None
    reviews = ReviewRating.objects.filter(
        product_id=single_product.id, status=True)
    else:
        order_product = None
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
        'orderproduct': orderproduct,
        'reviews': reviews,
    }
    return render(request, 'product_detail.html', context)


def search(request):
    # Search view
    products = []
    product_count = []
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by(
                '-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'product_count':  product_count,
    }
    return render(request, 'index.html', context)
