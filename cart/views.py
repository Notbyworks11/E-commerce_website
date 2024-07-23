from django.shortcuts import render,get_object_or_404,redirect
from .cart import Cart
from core.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    #get the cart
    cart = Cart(request)
    cart_products= cart.get_prods
    return render(request,'Products/cart_summary.html',{"cart_products": cart_products})
def cart_add(request):
    #Get cart
    cart = Cart(request)
    #test for POST
    if request.POST.get('action') == 'post':
        #GET stuff
        product_id =int(request.POST.get('product_id'))
        #lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        #save to session
        cart.add(product=product)
        #get cart_quantity
        cart_quantity = cart.__len__()

        #return response
        #response =JsonResponse({'Product Name': product.name})
        response =JsonResponse({'qty': cart_quantity})
        return response

def clear_cart_view(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_summary')

def cart_delete(request):
    pass
def cart_update(request):
    pass