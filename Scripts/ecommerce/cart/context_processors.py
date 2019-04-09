from .cart import Cart # import our cart Cart class

def cart(request): # create a python function called cart which takes request as a parameter
    return {'cart': Cart(request)} # return a python dictionary which will be available to all templates render using request context