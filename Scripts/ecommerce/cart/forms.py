from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26)]
# we create a range that start from 1 to 26. We will use this as drop down for user to select number of items.

# create a class that we will use to add items to the cart
class CartAddProductForm(forms.Form):
    # we define a quantity field in the form and we pass our choices from line 3
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    # define an update field that will help in either adding or updating number of item to the cart
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)