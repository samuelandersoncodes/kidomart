from django.db import models
from django.urls import reverse


class Category(models.Model):
    """
    Creates category fields
    """

    category_name = models.CharField(max_length=35, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    description = models.TextField(max_length=100, blank=True)
    category_image = models.ImageField(
        upload_to='images/categories', blank=True)

    class Meta:
        # Correctly pluralize the category word
        verbose_name_plural = 'Categories'

    def get_url(self):
        # Dynamically generates category url by slug
        return reverse('products_category', args=[self.slug])

    def __str__(self):
        return self.category_name