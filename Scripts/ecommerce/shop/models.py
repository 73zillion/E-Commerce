from django.db import models
from django.urls import reverse # import reverse function from django urls

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    ceated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    # create get_absolute_url method to create SEO-friendly url from our shop url patterns.
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),) #  using index_together meta option to specify an index for id and slug fields. This will help improve performances of queries.

    def __str__(self):
        return self.name

    # created get_absolute_url method to create SEO-friendly url from our shop url patterns. Remember the app_name we defined in the shop app urls.py file, that is how we use it in the get_absolute_url()
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])