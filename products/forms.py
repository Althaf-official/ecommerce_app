from django import forms


from .models import Product

class ProductForm(forms.ModelForm):

    title          = forms.CharField(
        label='',
        # required=True is default
        widget=forms.TextInput(
            attrs={
                "placeholder":"your title"
                }))
    description    = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder":"your Description",
                "class": "new-class-name two",
                "rows": "20",
                "cols": "50",
                "id": "my-sample-id",
            }
        ))
    price          = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get("title")
        if "MAS" in title:
            return title
        else:
            raise forms.ValidationError("this is not a valid title")



class RawProductForm(forms.Form):
    title          = forms.CharField(
        label='',
        # required=True is default
        widget=forms.TextInput(
            attrs={
                "placeholder":"your title"
                }))
    description    = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder":"your Description",
                "class": "new-class-name two",
                "rows": "20",
                "cols": "50",
                "id": "my-sample-id",
            }
        ))
    price          = forms.DecimalField(initial=200)