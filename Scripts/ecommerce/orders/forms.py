from django import forms # import django forms
from .models import Order # import Order class from orders models.py file

# create OrderCreateForm form using django forms model
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order # define which model to use, in this case we use Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city'] # define form field as specified in our Order model