from decimal import Decimal # import decimal data type in order to avoid issue of rounding off with regard to price

from django.conf import settings # import our settings configuration located in the settings.py file

from shop.models import Product # import our product model from our shop application

# create a cart class that will help us manage our shopping cart
class Cart(object):
    #  require the cart to be initialized with request object
    def __init__(self, request):
            self.session = request.session # tore the current session using self.session = request.session and this help in making sure that the cart is available for other method in our Cart class.

            cart = self.session.get(settings.CART_SESSION_ID) # try to get the cart using get method in the current session

            # If there is not cart in the session, we set an empty cart on line 17 by settings an empty dictionary in the session.
            if not cart:
                cart = self.session[settings.CART_SESSION_ID] = {}
            self.cart = cart

    # We create a method to add product into our cart. The add method takes ( self, product, quantity=1, update_quantity=False) as it’s parameters
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id) # use product_id as the key in the cart content dictionary, we convert product id into a string because Django uses json to serialize session data and json only allows string names

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'price': str(product.price)} # The product id is the key and the value we persist is the a dictionary with quantity and price of the product. We also convert the price of the product to string in order to serialize it

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save() # save the cart in the session

    # We create save method which tracks changes in the cart and marks sessions as modified using self.session.modified = True
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    # create a method to remove a single product from the cart and save the cart in the session.
    def remove(self, product):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # define an __iter__ (self) method which help us iterate through the items in contained in our cart and get the related product instances.
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    # define a len method to return the total number of items store in our cart
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    # define get_total_price method to get the total cost of the items in the cart
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    # define a method to clear the cart session
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True