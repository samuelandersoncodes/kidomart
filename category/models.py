from django.db import models

class Category(models.Model):
    """
    Creates category fields
    """
    class Meta:
        # Correctly pluralize the category word
        verbose_name_plural = 'Categories'

    category_name models.Charfield(max_length=35, unique=True)
    slug = models.Charfield(max_length=60, unique=True)
    description = models.TextField(max_length=100, blank=True)
    category_image = models.ImageField(updload='images/categories', blank=True)

    def __str__(self):
        return self.category_name
