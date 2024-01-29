from pages.views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('home/detail', detail, name='detail'),
    path('home/cart', cart, name='cart')
]