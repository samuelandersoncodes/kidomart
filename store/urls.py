from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('category/<slug:category_slug>/',
         views.home, name='products_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/',
         views.product_detail, name='product_detail'),
]
