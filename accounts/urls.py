from django.urls import path, include
from .views import AccountDeleteView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('reset_password_validate/<uidb64>/<token>/',
         views.reset_password_validate, name='reset_password_validate'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('order_detail/<str:order_id>/',
         views.order_detail, name='order_detail'),
    path('delete_account/', AccountDeleteView.as_view(), name='delete_account'),
    path('password_change_success', views.password_change_success,
         name='password_change_success'),
]
