from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product, ProductVariation
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist


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
    product = Product.objects.get(item_id=item_id)
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

        cart_id = request.session.session_key
        if not cart_id:
            request.session.create()
            cart_id = request.session.session_key

        try:
            cart = Cart.objects.get(cart_id=cart_id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=cart_id)
            cart.save()

        cart_item_exists = CartItem.objects.filter(
            product=product, cart=cart). exists()
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
                item = CartItem.objects.get(product=product, id=cart_item_id)
                item.quantity += 1
                item.save()
            else:
                item = CartItem.objects.create(
                    product=product, quantity=1, cart=cart)
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variation.add(*product_variation)
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
        cart_id = request.session.session_key
        cart = Cart.objects.get(cart_id=cart_id)
        product = get_object_or_404(Product, item_id=item_id)

        try:
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
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, item_id=item_id)
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


def checkout(request, total=0, quantity=0, cart_items=None):
    """
    This function retrieve the cart based on the current session
    And also retrieves active cart items associated with the cart
    It arranges the checkout cart items in descendning order
    It then calculates the tax, total price and quantity of checked out items
    And renders the template with the calculated context
    """
    try:
        tax = 0
        grand_total = 0
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
    return render(request, 'checkout.html', context)
