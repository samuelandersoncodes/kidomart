from django.shortcuts import render, redirect
from carts. models import CartItem
from .forms import OrderForm
from .models import Order
import datetime


def payments(request):
    # Payments view
    return render(request, 'payments.html')


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
            context = {
                'order': order,
                'cart_items': cart_items,
                'total': total,
                'tax': tax,
                'grand_total': grand_total,
            }
            return render(request, 'payments.html', context)
        else:
            return redirect('checkout')
    else:
        return redirect('checkout')
