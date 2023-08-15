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
    # email     = forms.EmailField()
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

    # def clean_title(self,*args,**kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "alt" in title:
    #         raise forms.ValidationError("this is not a valid title")
    #     if not "Muh" in title:
    #         raise forms.ValidationError("this is not a valid title")
    #     if not "Jas" in title:
    #         raise forms.ValidationError("this is not a valid title")
    #     return title
    
    # def clean_email(self,*args,**kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("this is not a valid email")
    #     return email



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