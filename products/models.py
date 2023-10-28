from django.db import models
from category.models import Category

class Product(models.Model):
    """
    Creates fields for products 
    """
    product_name = models.CharField(max_length=30,  unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='other')
    item_id = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField(max_length=60, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        # Returns actual product name
        return self.product_name
