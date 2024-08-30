from django import forms

class ClothingItemForm(forms.Form):
    shirt_url = forms.URLField(label='Shirt URL', max_length=200)
    pants_url = forms.URLField(label='Pants URL', max_length=200)
