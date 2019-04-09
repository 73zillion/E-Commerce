from django.shortcuts import render # import django render function to assist show our template
from .models import OrderItem # import our OrderItem model from our orders application
from .forms import OrderCreateForm #  import our OrderCreateForm form from forms.py file of orders application
from cart.cart import Cart # import our Cart class from our cart application

# create order_create(request) method which will process our order
def order_create(request):
    cart = Cart(request) # obtain the current cart from the session using Cart(request)
    if request.method == 'POST': # check whether the form is being submitted using post method
        form = OrderCreateForm(request.POST) # create an instance of OrderCreateForm
        if form.is_valid(): # check whether the form is valid
            order = form.save() # create a variable order and we save the order
            
            # create a for loop where we are looping through all the item in the shopping cart
            for item in cart:
                #  use our OrderItem model to save each item in our cart using create method
                OrderItem.objects.create(
                    order=order, # access our order instance
                    product=item['product'], # access the product from our cart instance
                    price=item['price'], # access the price of the product from our cart instance
                    quantity=item['quantity'] # access the quantity of the product from our cart instance
                )
            cart.clear() # after saving our order we clear our cart
        return render(request, 'orders/order/created.html', {'order': order}) # render a success page showing customer order was created successfully and we pass the order to this template.
    else:
        form = OrderCreateForm() # if the request was a get, we create an instance of OrderCreateForm form
    return render(request, 'orders/order/create.html', {'form': form}) # return the template where the use will see the form to fill