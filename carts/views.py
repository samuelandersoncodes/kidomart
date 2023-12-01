from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.conf import settings
from products.models import Product, ProductVariation
from orders.forms import OrderForm
from orders.models import Order, OrderProduct
import datetime
from .models import Cart, CartItem
from orders.forms import OrderForm
from orders.views import place_order
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
import stripe


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


def add_to_cart(request, item_id):
    """
    View for adding a product to the cart
    It gets the product object based on the provided product ID
    And tries to retrieve an existing cart for the current session
    If no cart exists, it creates a new one with the current session's cart ID
    And saves existing or newly created cart
    It also tries to retrieve an existing cart item for the given product and cart
    If the item exists, it increments its quantity
    If no cart item exists, it creates a new one with quantity 1
    It the posts products with associated variations
    And finally Redirect the user to the 'cart' page after adding the item
    """
    current_user = request.user
    product = Product.objects.get(item_id=item_id)
    if current_user.is_authenticated:
        product_variation = []
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]
                try:
                    variation = ProductVariation.objects.get(
                        product=product, variation_category__iexact=key, variation_value__iexact=value)
                    product_variation.append(variation)
                except:
                    pass
            cart_item_exists = CartItem.objects.filter(
                product=product, user=current_user).exists()
            if cart_item_exists:
                cart_item = CartItem.objects.filter(
                    product=product, user=current_user)
                old_variation_list = []
                id = []
                for item in cart_item:
                    existing_variation = item.variations.all()
                    old_variation_list.append(list(existing_variation))
                    id.append(item.id)
                if product_variation in old_variation_list:
                    index = old_variation_list.index(product_variation)
                    cart_item_id = id[index]
                    item = CartItem.objects.get(
                        product=product, id=cart_item_id)
                    item.quantity += 1
                    item.save()
                else:
                    item = CartItem.objects.create(
                        product=product, quantity=1, user=current_user)
                    if len(product_variation) > 0:
                        item.variations.clear()
                        item.variations.add(*product_variation)
                    item.save()
            else:
                cart_item = CartItem.objects.create(
                    product=product,
                    quantity=1,
                    user=current_user,
                )
                if len(product_variation) > 0:
                    cart_item.variations.clear()
                    cart_item.variations.add(*product_variation)
                cart_item.save()
        return redirect('cart')
    else:
        product_variation = []
        if request.method == 'POST':
            for item in request.POST:
                key = item
                value = request.POST[key]
                try:
                    variation = ProductVariation.objects.get(
                        product=product, variation_category__iexact=key, variation_value__iexact=value)
                    product_variation.append(variation)
                except:
                    pass
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
            except Cart.DoesNotExist:
                cart = Cart.objects.create(
                    cart_id=_cart_id(request)
                )
                cart.save()
            cart_item_exists = CartItem.objects.filter(
                product=product, cart=cart).exists()
            if cart_item_exists:
                cart_item = CartItem.objects.filter(product=product, cart=cart)
                old_variation_list = []
                id = []
                for item in cart_item:
                    existing_variation = item.variations.all()
                    old_variation_list.append(list(existing_variation))
                    id.append(item.id)
                if product_variation in old_variation_list:
                    index = old_variation_list.index(product_variation)
                    cart_item_id = id[index]
                    item = CartItem.objects.get(
                        product=product, id=cart_item_id)
                    item.quantity += 1
                    item.save()
                else:
                    item = CartItem.objects.create(
                        product=product, quantity=1, cart=cart)
                    if len(product_variation) > 0:
                        item.variations.clear()
                        item.variations.add(*product_variation)
                    item.save()
            else:
                cart_item = CartItem.objects.create(
                    product=product,
                    quantity=1,
                    cart=cart,
                )
                if len(product_variation) > 0:
                    cart_item.variations.clear()
                    cart_item.variations.add(*product_variation)
                cart_item.save()
        return redirect('cart')


def remove_from_cart(request, item_id, remove_cart_item_id):
    """
    View for decreasing product quantity in the cart
    It gets the Cart object associated with the current session
    And gets the Product object with the specified item_id or raise a 404 error if not found
    It then gets the CartItem associated with the Cart and Product
    and check if cart item quantity is more than one
    If the quantity is one or less, it removes the cart item
    And redirects user to cart page after removing item
    """
    if request.method == 'POST':
        cart_id = _cart_id(request)
        product = get_object_or_404(Product, item_id=item_id)
        try:
            if request.user.is_authenticated:
                cart_item = CartItem.objects.get(
                    product=product, user=request.user, id=remove_cart_item_id)
            else:
                cart = Cart.objects.get(cart_id=cart_id)
                cart_item = CartItem.objects.get(
                    product=product, cart=cart, id=remove_cart_item_id)
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
        except:
            pass
    return redirect('cart')


def delete_cart_item(request, item_id, remove_cart_item_id):
    """
    Cart item removal view
    It gets the Cart object associated with the current session
    And gets the Product object with the specified item_id or raise 404 error
    Deletes the cart item and returns to cart page
    """
    product = get_object_or_404(Product, item_id=item_id)
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(
            product=product, user=request.user, id=remove_cart_item_id)
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(
            product=product, cart=cart, id=remove_cart_item_id)
    cart_item.delete()
    return redirect('cart')


def cart(request, total=0, quantity=0, cart_items=None):
    """
    View to display cart template
    It tries to retrieve the cart based on the current session
    And also retrieves active cart items associated with the cart
    It arranges the cart items in descendning order
    It then calculates the tax, total price and quantity of items in the cart
    And renders the template with the calculated context
    """
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(
                user=request.user, is_active=True).order_by('-id')
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(
                cart=cart, is_active=True).order_by('-id')
        for cart_item in cart_items:
            if cart_item.product.on_sale:
                total += (cart_item.product.sale_price * cart_item.quantity)
            else:
                total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (1 * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'cart.html', context)


@login_required(login_url='login')
def checkout(request, total=0, quantity=0, cart_items=None):
    """
    This function retrieve the cart based on the current session
    And also retrieves active cart items associated with the cart
    It arranges the checkout cart items in descendning order
    It then calculates the tax, total price and quantity of checked out items
    The function checks and saves the order form.
    Payment is then made via stripe.
    And template is rendered with the calculated context
    upon a successful payment, user is redirected to the checkout success page
    """
    data = Order()
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
    order_form = OrderForm()
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            data = Order()
            data.user = current_user
            data.first_name = order_form.cleaned_data['first_name']
            data.last_name = order_form.cleaned_data['last_name']
            data.email = order_form.cleaned_data['email']
            data.tel = order_form.cleaned_data['tel']
            data.address_line_1 = order_form.cleaned_data['address_line_1']
            data.address_line_2 = order_form.cleaned_data['address_line_2']
            data.country = order_form.cleaned_data['country']
            data.state = order_form.cleaned_data['state']
            data.city = order_form.cleaned_data['city']
            data.order_note = order_form.cleaned_data['order_note']
            data.tax = round(tax, 2)
            grand_total = round(total + tax, 2)
            order_total = grand_total
            data.order_total = round(grand_total, 2)
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime('%Y%d%m')
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()
            order = Order.objects.get(
                user=current_user, is_ordered=False, order_number=order_number)
            order.is_ordered = True
            order.save()
            for cart_item in cart_items:
                order_product = OrderProduct.objects.create(
                    user=order.user,
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    product_price=cart_item.product.price,
                    ordered=True,
                )
                order_product.variations.set(cart_item.variations.all())
                cart_item.save()
            cart_items.update(is_active=False)
            tax = data.tax
            order_total = data.order_total
            messages.success(request, 'Your order was successful!')
            return redirect('checkout_success', order_number=data.order_number)
        else:
            messages.error(
                request, 'Please check your details and resubmit')
            return redirect('checkout')
    else:
        try:
            tax = round((1 * total) / 100, 2)
            order_total = round(total + tax, 2)
            amount_in_cents = int(grand_total * 100)
            # Ensure the amount is at least 50 cents
            if amount_in_cents < 50:
                amount_in_cents = 50
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=amount_in_cents,
                currency=settings.STRIPE_CURRENCY,
                payment_method_types=['card'],
            )
        except ObjectDoesNotExist:
            pass
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'order_total': order_total,
        'stripe_public_key': stripe_public_key,
        'stripe_secret_key': stripe_secret_key,
        'client_secret': intent.client_secret,
        'order_form': order_form,
    }
    return render(request, 'checkout.html', context)


def checkout_success(request, order_number):
    """
    This function retrieves the order by order_number
    It also retrieves ordered products and associated cart
    items for the current user, transfers cart items to 
    order products and update product stock and 
    clears the user's cart and cart count
    """
    order = Order.objects.get(order_number=order_number)
    order_products = OrderProduct.objects.filter(order=order)
    cart_items = CartItem.objects.filter(user=request.user)
    for item in cart_items:
        orderproduct = OrderProduct()
        orderproduct.order_id = order.id
        orderproduct.user = request.user
        orderproduct.product_id = item.product_id
        orderproduct.quantity = item.quantity
        orderproduct.product_price = item.product.price
        orderproduct.ordered = True
        orderproduct.save()
        cart_item = CartItem.objects.get(id=item.id)
        product_variation = cart_item.variations.all()
        orderproduct = OrderProduct.objects.get(id=orderproduct.id)
        orderproduct.variations.set(product_variation)
        orderproduct.save()
        product = Product.objects.get(id=item.product_id)
        product.stock -= item.quantity
        product.save()
    CartItem.objects.filter(user=request.user).delete()
    cart_count = CartItem.objects.filter(user=request.user, quantity__gt=0).count()
    context = {
        'order': order,
        'order_products': order_products,
        'cart_count': cart_count,
    }
    return render(request, 'checkout_success.html', context)
