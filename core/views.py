from django.shortcuts import render,HttpResponse, redirect
from .models import Product, Category
from  django.contrib.auth import login, authenticate ,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
# Create your views here.

def index(request):
    products = Product.objects.all()
    return render( request, "Home/home.html",{'products':products})

def about(request):
    return render(request,"Home/about.html",{})

def product(request,pk): 
    product = Product.objects.get(id=pk)
    return render( request, "Products/product.html",{'product':product})

def category(request,foo):
    #replacing hyphens with spaces
    foo =foo.strip().replace('-',' ')
    #Call category from the url
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category = category)
        
        return render(request,'Products/category.html',{'products':products, 'category':category})
    except Category.DoesNotExist:
        # Handle the case where the category doesn't exist
        messages.error(request, f'The category "{foo}" does not exist.')
        # Consider redirecting to a different page or rendering a specific template for this case
        return redirect('index')
    except Exception as e:
        # Handle other exceptions (e.g., database connection issues)
        messages.error(request, f'Error occurred: {str(e)}')
        # Redirect to a generic error page or handle as appropriate
        return redirect('index')
       


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
