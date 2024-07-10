from django.shortcuts import render,HttpResponse, redirect
from .models import Product
from  django.contrib.auth import login, authenticate ,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render( request, "products/products.html",{'products':products})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username ,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("You have been logged in.... "))
            return redirect('index')
        else:
            messages.success(request,("There was an error, please try again ....."))
            return redirect('login')
    else:
        return render(request,'Logs/Login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,("You have been logged out ....."))
    return redirect('index')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #log in user 
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have successfully created an account'))
            return redirect('index')
        else:
            messages.success(request,('Whoops !! There was a problem'))
            return redirect('register')
    else:
        return render(request, 'Logs/Register.html',{'form':form})
