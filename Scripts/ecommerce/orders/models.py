from django.db import models # import django database model
from shop.models import Product # import the product model located in the shop model

# create Order class where we capture customer details
class Order(models.Model):
    # capture customer details which include first name, last name, email, address, postal code, city, created date and updated date
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False) # create a boolean field which we set default to false. This field is important since we can use this field to differentiate between paid and unpaid orders

    # create a meta class which we order our orders by the date created
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    # define get_total_cost() method which we obtain the total cost of a given order
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

# define OrderItem model which will allow us to store order, product, price per item and quantity
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    # define get_cost() method where we multiply price and quantity of the products
    def get_cost(self):
        return self.price * self.quantity