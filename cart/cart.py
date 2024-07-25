from core.models import Product
class Cart():
    def __init__(self, request):
        self.session = request.session
        # Use a consistent key name for the cart in the session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
    def add(self, product, quantity, update_quantity=False):
        product_id = str(product.id)
        product_qty = int(quantity)
        if product_id in self.cart:
            if update_quantity:
                self.cart[product_id]['quantity'] = (product_qty)
            else:
                self.cart[product_id]['quantity'] += (product_qty)
        else:
            self.cart[product_id] = {'price': str(product.price), 'quantity': quantity}
        self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def clear(self):
        # Clear the cart in the session
        self.cart = {}
        self.session['cart'] = self.cart
        self.session.modified = True
    
    def get_prods(self):
        #get ids from cart
        product_ids = self.cart.keys()
        #lookfor product using the ids
        products = Product.objects.filter(id__in=product_ids)
        
        return products
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product , quantity):
        product_id =str(product)
        product_qty = int(quantity)
         
        ourcart = self.cart

        #update Dictionary
        ourcart[product_id]['quantity'] = product_qty

        self.save()
        #update cart
        upcart = self.cart

        return upcart
    
    def delete(self,product):
        product_id  = str(product)
        rcart = self.cart
        if product_id in self.cart:
            del rcart[product_id]
            
        self.save()
        #removed item and updated cart
        rucart = self.cart
        return rucart
        

