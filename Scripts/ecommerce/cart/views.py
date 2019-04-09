from django.shortcuts import render, redirect, get_object_or_404 # import django shortcuts to helps render, redirect and query our database
from django.views.decorators.http import require_POST # import django decorator to post our form
from shop.models import Product # import our Product model from our shop
from .cart import Cart # import our Cart class from cart.py file
from .forms import CartAddProductForm # import our form from forms.py file

@require_POST #use @require_POST decorator to make sure that only post request are allowed
def cart_add(request, product_id): # define a method to add items to the Cart. This method takes product id as a parameters
    cart = Cart(request) # create a cart object by passing request to our cart class
    product = get_object_or_404(Product, id=product_id) # we retrieve our product from database based on the product id
    form = CartAddProductForm(request.POST) # validated our form from the request

    # if our form is valid we add our item to the cart and update our cart
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])

    return redirect('cart:cart_detail') # redirect our cart to cart detail page

def cart_remove(request, product_id): # define a method to remove items from the cart. This method takes product id as a parameter
    cart = Cart(request) # create a cart object from our request
    product = get_object_or_404(Product, id=product_id) #  retrieve product by id
    cart.remove(product) # remove item from our shopping cart
    return redirect('cart:cart_detail') # redirect user to our cart detail page

def cart_detail(request): # define a method to display our cart detail page
    cart = Cart(request) # create a cart object from our request

    # create a for loop to iterate through all products in the cart
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity':item['quantity'], 'update': True})

    return render(request, 'cart/detail.html', {'cart':cart}) # render a template called detail.html