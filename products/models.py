import uuid
from django.db import models
from category.models import Category
from accounts.models import Account
from django.db.models import Avg

def generate_item_id():
    # Customizes a product id for each product
    prefix = 'kidoprod'  # Custom prefix for products
    unique_id = str(uuid.uuid4())  # Generate a unique identifier
    return f'{prefix}-{unique_id}'


class Product(models.Model):
    """
    Creates fields for products 
    """
    product_name = models.CharField(max_length=30,  unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default='other')
    item_id = models.CharField(
        max_length=50, unique=True, default=generate_item_id)
    description = models.TextField(max_length=60, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
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

    def averageReview(self):
        """
        This function filters the products
        Finds its average rating and checks
        if there is a rating, if ther is,
        Rating is coverted to float
        """
        reviews = ReviewRating.objects.filter(
            product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg


class VariationManager(models.Manager):
    # Custom product variation manager class
    def colors(self):
        # Retrieves color variation
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        # Retrieves size variation
        return super(VariationManager, self).filter(variation_category='size', is_active=True)


# Variation choices
variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)


class ProductVariation(models.Model):
    """
    Creates fields for product variations
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(
        max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value


class ReviewRating(models.Model):
    # Review and rating model
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField(default=0.0)
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
