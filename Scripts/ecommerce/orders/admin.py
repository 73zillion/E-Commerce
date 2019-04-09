from django.contrib import admin # import django admin model
from .models import Order, OrderItem # import the Order and OrderItem model from orders models.py file

# create OrderItemInline class which we use tabularInline
class OrderItemInline(admin.TabularInline):

    # use our OrderItem item model and create a raw id field for product
    model = OrderItem
    raw_id_fields = ['product']

# create OrderAdmin class
class OrderAdmin(admin.ModelAdmin):

    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', 'created' ,'updated'] # create a list display of the customer
    list_filter = ['paid', 'created', 'updated'] # create a list filter using paid, created and updated fields
    inlines = [OrderItemInline] # include our OrderItemInline class as an inline. An inline allows you to include a model for appearing on the same edit page as the parent model

admin.site.register(Order, OrderAdmin) # register our models in django admin site
