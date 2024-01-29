from blog.views import blog
from django.urls import path


urlpatterns = [
    path('',blog, name='blog'),
]