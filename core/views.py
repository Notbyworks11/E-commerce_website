from django.shortcuts import render,HttpResponse
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render( request, "core/home.html",{'products':products})