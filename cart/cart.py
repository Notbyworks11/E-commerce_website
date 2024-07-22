class Cart():
    def __init__(self, request):
        self.session = request.session
        # Use a consistent key name for the cart in the session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id in self.cart:
            if update_quantity:
                self.cart[product_id]['quantity'] = quantity
            else:
                self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {'price': str(product.price), 'quantity': quantity}
        self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())