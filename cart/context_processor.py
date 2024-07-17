from .cart import Cart

# Create context processor to aid in the cart working on all pages

def cart( request):
    #Return the default data from Cart
    return {'cart':Cart(request)}