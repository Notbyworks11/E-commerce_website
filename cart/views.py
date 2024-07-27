from django.shortcuts import render,get_object_or_404,redirect
from .cart import Cart
from core.models import Product
from django.http import JsonResponse
from django.contrib  import messages

# Create your views here.
def cart_summary(request):
    #get the cart
    cart = Cart(request)
    cart_products= cart.get_prods
    quantities= cart.get_quants
    totals = cart.total()
    return render(request,'Products/cart_summary.html',{"cart_products": cart_products, "quantities":quantities,'totals':totals})
def cart_add(request):
    #Get cart
    cart = Cart(request)
    #test for POST
    if request.POST.get('action') == 'post':
        #GET stuff
        product_id =int(request.POST.get('product_id'))
        product_qty=int(request.POST.get('product_qty'))
        #lookup product in DB
        product = get_object_or_404(Product, id=product_id)
        #save to session
        cart.add(product=product, quantity =product_qty)
        #get cart_quantity
        cart_quantity = cart.__len__()

        #return response
        #response =JsonResponse({'Product Name': product.name})
        response =JsonResponse({'qty': cart_quantity})
        messages.success(request,("Product Added To Cart "))
        return response

def clear_cart_view(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_summary')

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
         product_id =int(request.POST.get('product_id'))
         cart.delete(product = product_id)
         response = JsonResponse({'product':product_id})
         messages.success(request,("Item Removed from Cart...."))
         return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        #GET stuff
        
        product_id =int(request.POST.get('product_id'))
        product_qty=int(request.POST.get('product_qty'))
        print('Product ID:', product_id)  # Debugging
        print('Product Quantity:', product_qty)  # Debugging
        cart.update( product = product_id , quantity = product_qty )

        response = JsonResponse({'qty':product_qty})
        messages.success(request,("Your Cart Has Been Updated... "))
        return response
        #return redirect('cart_summary')