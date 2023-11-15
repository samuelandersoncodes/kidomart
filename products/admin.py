from django.contrib import admin
from .models import Product, ProductVariation


class ProductAdmin(admin.ModelAdmin):
    # Displays specified fields and prepopulates slug
    list_display = (
        'product_name',
        'price',
        'stock',
        'category',
        'created_date',
        'modified_date',
        'is_available'
    )
    prepopulated_fields = {
        'slug': ('product_name',)
    }


admin.site.register(Product, ProductAdmin)

admin.site.register(ProductVariation)
