from django.conf.urls import url # import django url helper class
from . import views # import views from cart views.py file

app_name = 'cart' # create a namespace for our cart application called ‘cart’

# we create a list of url patterns
urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'), # define a url that will display cart detail page
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'), # define url to add items to the cart
    url(r'remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'), #  define url to remove items from our cart
]