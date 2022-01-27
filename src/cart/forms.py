from django import forms
from.models import ColourVariation, OrderItem, Product, SizeVariation
class AddToCartForm(forms.ModelForm):
    colour= forms.ModelChoiceField(queryset= ColourVariation.objects.none())
    size= forms.ModelChoiceField(queryset= SizeVariation.objects.none())
    class Meta:
        model =OrderItem
        fields =['quantity','colour','size']
    
    def __init__(self,*arg,**kwargs):
        product_id= kwargs.pop('product_id')
        product =Product.objects.get(id=product_id)
        super().__init__(*arg,**kwargs)

        self.fields['colour'].queryset=product.available_colours.all()
        self.fields['size'].queryset=product.available_sizes.all()