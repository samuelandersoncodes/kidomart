from django.contrib import admin
from .models import Payment, Order, OrderProduct


class OderAdmin(admin.ModelAdmin):
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


admin.site.register(Order, OderAdmin)
admin.site.register(OrderProduct)
admin.site.register(Payment)
