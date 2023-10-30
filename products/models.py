import uuid
from django.db import models
from category.models import Category


def generate_item_id():
    # Customizes a product id for each product
    prefix = 'kidoprod'  # Custom prefix for products
    unique_id = uuid.uuid4().hex[:10]  # Generate a unique identifier
    return f'{prefix}-{unique_id}'

class Product(models.Model):
    """
    Creates fields for products 
    """
    product_name = models.CharField(max_length=30,  unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='other')
    item_id = models.CharField(max_length=50, unique=True, default=generate_item_id)
    description = models.TextField(max_length=60, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        # Returns actual product name
        return self.product_name
