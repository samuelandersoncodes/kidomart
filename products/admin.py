from django.contrib import admin
from .models import Product, ProductVariation, ReviewRating


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


class ProductVariationAdmin(admin.ModelAdmin):
    # Displays specified product variation fields
    list_display = (
        'product',
        'variation_category',
        'variation_value',
        'is_active'
    )
    list_editable = ('is_active',)
    list_filter = (
        'product',
        'variation_category',
        'variation_value',
        'is_active'
    )


admin.site.register(Product, ProductAdmin)

admin.site.register(ProductVariation, ProductVariationAdmin)

admin.site.register(ReviewRating)
