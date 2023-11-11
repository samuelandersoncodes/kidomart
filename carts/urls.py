from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_cart/<str:item_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<str:item_id>/', views.remove_cart, name='remove_cart'),
    path('delete_cart_item/<str:item_id>/', views.delete_cart_item, name='delete_cart_item'),
]