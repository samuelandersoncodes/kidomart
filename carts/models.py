from django.db import models
from products.models import Product

class Cart(models.Model):
    # Shopping cart model
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        # Returns the cart_id as the string representation
        return self.cart_id


class CartItem(models.Model):
    # Model representing item within the shopping cart
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        # Returns the product as the string representation
        return self.product
