from django.shortcuts import render

from .forms import ProductForm,RawProductForm

from .models import Product
# Create your views here.

def dynamic_lookup_view(request, my_id):
    obj = Product.objects.get(id=my_id)
    context = {
        "object": obj
        }
    return render(request, "products/product_detail.html", context)


def render_initial_data(request):
    initial_data = {
        'title': "my awe title"
    }
    obj = Product.objects.get(pk=13)
    form = ProductForm(request.POST or None, instance=obj)
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)



# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)#!By using **, you're unpacking the dictionary's contents and passing them as keyword arguments to the create() method.
#             my_form=RawProductForm()
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form,
#     }
#     return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     #print(request.GET)
#     #print(request.POST)
#     if request.method == "POST":
#         my_new_title=request.POST.get("title")
#         print(my_new_title)
#         #Product.objects.create(title=my_new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()#!After successfully saving the form data, a new, empty instance of ProductForm is created. This step is likely intended to clear the form for a new input after successful submission. It ensures that the form fields are empty and ready to receive new data for the next submission.
        
    
    context = {
        'form': form,
    }

    return render(request, "products/product_create.html", context)



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
