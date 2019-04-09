from django.conf.urls import url # import django url
from . import views # import orders views

app_name = 'orders' # create a namespace for our orders application

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create') # create a url pattern that goes to order_create method in orders views.py file
]