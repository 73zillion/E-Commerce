from django.shortcuts import render, get_object_or_404 # importing shortcut methods to render my template and to check whether an object is found or to raise a 404 error.

from .models import Category, Product # importing my Category and Product model.

from cart.forms import CartAddProductForm # import CartAddProductForm package from cart forms


 # creating a function called product_list which I will use to display a list of products. In this function, I am also passing a second parameter called category_slug=None which I will use if products are filtered using a given category by our users.
def product_list(request, category_slug=None):
    category = None # specifying category is equal to none, in order to show the list of products without filtering them by any category.

    categories = Category.objects.all() # querying and fetching all the categories from my database

    products = Product.objects.filter(available=True) # fetching all the products from my database which are available by passing(available=True) filter to my queryset.


    # creating an if statement to optionally filter the products based on the category_slug parameter passed from my url.
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug) # creating a variable called category and creating a queryset to the Category model and filtering the result with category_slug parameter.

        products = Product.objects.filter(category=category) # creating a queryset to fetching products and filtering the products based on the category from line 12


   # simply creating a data dictionary to pass to my template.
    context = {
        'category':category,
        'categories':categories,
        'products':products
    }
    return render(request, 'shop/product/list.html', context) #  rendering a template called list.html which there is yet to create and also passing data context.


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True) # creating queryset and I am using id and slug to retrieve product instance. That is also checking whether the product is available or not.
    # We can get this instance by just the ID since it’s a unique attribute. However, we include the slug in the URL to build SEO-friendly URLs for products.
    
    cart_product_form = CartAddProductForm() #  created our cart_product_form object

    # creating a dictionary of my data in order to pass this data to my template using a single context.
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'shop/product/detail.html', context) # rendering a template called detail.html which there is yet to create and passing the context data to this template.