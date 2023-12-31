from django.contrib import admin
from .models import Order, OrderProduct


class OrderProductInline(admin.TabularInline):
    # Tabulates product order details
    model = OrderProduct
    readonly_fields = (
        'user',
        'product',
        'quantity',
        'product_price',
        'ordered'
    )
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    # Displays product order list
    list_display = [
        'order_number',
        'full_name',
        'email',
        'tel',
        'city',
        'order_total',
        'tax',
        'status',
        'is_ordered',
        'created_at'
    ]
    list_filter = [
        'status',
        'is_ordered'
    ]
    search_fields = [
        'order_number',
        'first_name',
        'last_name',
        'email',
        'tel'
    ]
    list_per_page = 25
    inlines = [OrderProductInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
