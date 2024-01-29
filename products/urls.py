from products.views import products
from django.urls import path

urlpatterns = [
    path('', products, name='products'),
]