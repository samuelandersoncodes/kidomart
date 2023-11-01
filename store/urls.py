from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:category_slug>/', views.home, name='products_category'),
]
