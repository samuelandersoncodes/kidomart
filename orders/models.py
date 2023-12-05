from django.db import models
from accounts.models import Account
from products.models import Product, ProductVariation


class Order(models.Model):
    # Order model
    STATUS = (
        ('New', 'New'),
        ('Paid', 'Paid'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    order_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)
    email = models.EmailField(max_length=60)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    order_note = models.CharField(max_length=100, blank=True)
    order_total = models.FloatField()
    tax = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(max_length=20, blank=True)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def full_name(self):
        # full name concatenation
        return f'{self.first_name} {self.last_name}'

    def full_address(self):
        # full address concatenation
        return f'{self.address_line_1} {self.address_line_2}'

    def __str__(self):
        # user first name string representation
        return self.first_name


class OrderProduct(models.Model):
    # Order product model
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(ProductVariation, blank=True)
    quantity = models.IntegerField()
    product_price = models.FloatField()
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # user product name string representation
        return self.product.product_name
