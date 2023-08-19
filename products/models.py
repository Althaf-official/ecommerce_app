from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    price       = models.DecimalField(max_digits=100000,decimal_places=2)
    summary     = models.TextField(blank=True,null=False)
    features    = models.BooleanField(default=False)

def get_absolute_url(self):
    return f"/products/{self.id}/"
    #!when you call get_absolute_url() on an instance of the class where this method is defined, it will return a URL string that represents the absolute URL for that instance. For example, if you have a product with an id of 42, calling product.get_absolute_url() would return "/products/42/", which could be used to construct a link to that specific product's detail page in a Django web application.
    