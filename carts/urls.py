from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart/<str:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<str:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('delete_cart_item/<str:item_id>/', views.delete_cart_item, name='delete_cart_item'),
]