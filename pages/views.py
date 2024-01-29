from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html',)

def detail(request):
    return render(request, 'pages/single-product.html',)

def cart(request):
    return render(request, 'pages/shoping-cart.html',)