from django.shortcuts import render,HttpResponse
from .models import Product
from  django.contrib.auth import login, authenticate ,logout
from django.contrib import messages
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render( request, "products/products.html",{'products':products})

def login_user(request):
    return render(request,'Logs/Login.html',{})

def logout_user(request):
    pass