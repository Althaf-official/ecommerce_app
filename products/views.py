from django.shortcuts import render

from .models import Product
# Create your views here.

def product_detail_view(request):
    obj = Product.objects.get(id=6)
    # context = {
    #     "title": obj.title,
    #     "description": obj.description,
    # }
    context = {
        'object': obj#!associated with the key 'object' in the context dictionary. When you access context['object'], it returns the value
    }

    return render(request, "products/detail.html", context)
