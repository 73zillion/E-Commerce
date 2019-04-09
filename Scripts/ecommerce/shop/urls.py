from django.conf.urls import url # import url from django urls
from . import views # import methods in our views.py file

app_name = 'shop' # create a namespace for our shop application.

#  create a python list for our url patterns for our application.
urlpatterns = [
    url(r'^$', views.product_list, name='product_list'), # This url is mapped to our product_list method and it will fetch all products

    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    # This url is also mapped to product_list method but we pass category_slug as our parameter hence, products we be filtered by a given category.

    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    # This url is mapped to product_detail method and this will fetch a specific product.
]
