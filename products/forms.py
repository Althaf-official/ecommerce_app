from django import forms


from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    title          = forms.CharField(label='')# required=True is default
    description    = forms.CharField(required=False)
    price          = forms.DecimalField(initial=200)