from django.db import models
from products.models import Product, ProductVariation
from accounts.models import Account


class Cart(models.Model):
    # Shopping cart model
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        # Returns the cart_id as the string representation
        return self.cart_id


class CartItem(models.Model):
    # Model representing item within the shopping cart
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(ProductVariation, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    @property
    def sub_total(self):
        """
        This function defines a CartItem property
        And checks if the associated product is on sale
        It calculates the subtotal by multiplying
        either sale or regular price with the quantity respectively
        """
        if self.product.on_sale:
            return (self.product.sale_price) * self.quantity
        else:
            return (self.product.price) * self.quantity

    def __str__(self):
        # Returns the product as a string representation
        return str(self.product)
