from django.urls import path, include
from . import views

urlpatterns = [
    path('submit_review/<str:item_id>/',
         views.submit_review, name='submit_review'),
]
