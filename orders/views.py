from django.shortcuts import render, redirect
from carts. models import CartItem
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderProduct, Payment
from products.models import Product
import datetime
import json


def payments(request):
    """
    This function loads the request body JSON data
    Retrieves the order based on user, order status
    and order number from the request,
    Creates a Payment object with the
    received payment details
    Updates the order with the payment information
    and set it as ordered.
    It also processes each item in the user's cart
    and creates corresponding OrderProduct entries
    """
    body = json.loads(request.body)
    order = Order.objects.get(
        user=request.user, is_ordered=False, order_number=body['orderID'])
    payment = Payment(
        user=request.user,
        payment_id=body['transID'],
        payment_method=body['payment_method'],
        amount_paid=order.order_total,
        status=body['status'],
    )
    payment.save()
    order.payment = payment
    order.is_ordered = True
    order.save()
    cart_items = CartItem.objects.filter(user=request.user)
    for item in cart_items:
        orderproduct = OrderProduct()
        orderproduct.order_id = order.id
        orderproduct.payment = payment
        orderproduct.user_id = request.user_id
        orderproduct.product_id = item.product_id
        orderproduct.quantity = item.quantity
        orderproduct.product_price = item.product_price
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
    paypal_client_id = settings.PAYPAL_CLIENT_ID
    context = {
        'paypal_client_id': paypal_client_id
    }
    return render(request, 'payments.html', context)


def place_order(request, total=0, quantity=0):
    """
    This function processes the placement of an order.
    If there are no items in the user's cart, 
    It redirects the user to the cart page.
    """
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
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.email = form.cleaned_data['email']
            data.tel = form.cleaned_data['tel']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.tax = tax
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
            paypal_client_id = settings.PAYPAL_CLIENT_ID
            context = {
                'order': order,
                'cart_items': cart_items,
                'total': total,
                'tax': tax,
                'grand_total': grand_total,
                'paypal_client_id': paypal_client_id,
            }
            return render(request, 'payments.html', context)
        else:
            return redirect('checkout')
    else:
        return redirect('checkout')
