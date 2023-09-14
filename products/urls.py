from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<book_id>', views.book_detail, name='book_detail'),
]
