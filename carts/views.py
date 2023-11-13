from django.shortcuts import render, redirect, get_object_or_404
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
    And finally Redirect the user to the 'cart' page after adding the item
    """
    if request.method == 'POST':
        product = Product.objects.get(item_id=item_id)
        cart_id = request.session.session_key
        if not cart_id:
            request.session.create()
            cart_id = request.session.session_key

        try:
            cart = Cart.objects.get(cart_id=cart_id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=cart_id)
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


def remove_from_cart(request, item_id):
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
        cart_id = request.session.session_key
        cart = Cart.objects.get(cart_id=cart_id)
        product = get_object_or_404(Product, item_id=item_id)
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

    return redirect('cart')


def delete_cart_item(request, item_id):
    """
    Cart item removal view
    It gets the Cart object associated with the current session
    And gets the Product object with the specified item_id or raise 404 error
    Deletes the cart item and returns to cart page
    """
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, item_id=item_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
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
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True).order_by('-id')
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (1 * total)/100
        grand_total = total + tax
    except ObjectNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'cart.html', context)
