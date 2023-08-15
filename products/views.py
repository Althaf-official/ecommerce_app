from django.shortcuts import render

from .forms import ProductForm

from .models import Product
# Create your views here.

def product_create_view(request):
    context = {}
    return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()#!After successfully saving the form data, a new, empty instance of ProductForm is created. This step is likely intended to clear the form for a new input after successful submission. It ensures that the form fields are empty and ready to receive new data for the next submission.
        
    
#     context = {
#         'form': form,
#     }

#     return render(request, "products/product_create.html", context)



def product_detail_view(request):
    obj = Product.objects.get(id=6)
    # context = {
    #     "title": obj.title,
    #     "description": obj.description,
    # }
    context = {
        'object': obj#!associated with the key 'object' in the context dictionary. When you access context['object'], it returns the value
    }

    return render(request, "products/product_detail.html", context)
