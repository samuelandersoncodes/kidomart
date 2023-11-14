from .models import Cart, CartItem
from .views import _cart_id


def cart_counter(request):
    """
    This function initializes cart count at zero
    Checks if the request path contains 'admin'
    If the admin is in the path, it returns an empty dictionary
    It then tries to get the cart associated with the current user's session
    Gets all cart items related to the obtained cart
    It then loops through each cart item and increment
    the cart count by the quantity of each item
    If the cart does not exist, it sets cart count to zero
    And finally returns the cart count dictionary
    """
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)
