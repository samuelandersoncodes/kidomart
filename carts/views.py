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


def add_cart(request, item_id):
    """
    View for adding a product to the cart
    It gets the product object based on the provided product ID
    And tries to retrieve an existing cart for the current session
    If no cart exists, it creates a new one with the current session's cart ID
    And saves existing or newly created cart
    It also tries to retrieve an existing cart item for the given product and cart
    If the item exists, it increments its quantity
    If no cart item exists, it creates a new one with quantity 1
    And finally Redirect the user to the 'cart' page after adding the item
    """
    product = Product.objects.get(item_id=item_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )
        cart_item.save()

    return redirect('cart')


def cart(request, total=0, quantity=0, cart_items=None):
    """
    View to display cart template
    It tries to retrieve the cart based on the current session
    And also retrieves active cart items associated with the cart
    It then calculates the total price and quantity of items in the cart
    And renders the template with the calculated context
    """
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
    except ObjectNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context)
