from django import forms
from django.forms import widgets
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category_name']


class Laptopform(forms.ModelForm):
    class Meta:
        model = Laptop
        exclude = ['product']
        labels = {
            'ram':'RAM (Gb)',
            'rom':'ROM (Gb)',
            'price':'Price (Rs)',
            'limage':'Product Image',
            'brand_name':'Brand Name',
            'model_name':'Model Name',
            'warranty':'Warranty (Months)',
        }
        widgets = {
            'brand_name':forms.TextInput(attrs={'placeholder':'e.g. Sony'}),
            'model_name':forms.TextInput(attrs={'placeholder':'e.g. Pavellian'}),
            'processor':forms.TextInput(attrs={'placeholder':'e.g. i5 5th Generation'}),
            'ram':forms.TextInput(attrs={'placeholder':'e.g. 32'}),
            'rom':forms.TextInput(attrs={'placeholder':'e.g. 500'}),
            'price':forms.TextInput(attrs={'placeholder':'e.g. 40000'}),
            'quantity':forms.TextInput(attrs={'placeholder':'e.g. 30'}),
            'warranty':forms.TextInput(attrs={'placeholder':'e.g. 6 '}),   
        }

    def clean(self):
        all_data = super().clean()
        ram = all_data.get('ram')
        rom = all_data.get('rom')
        price = all_data.get('price')
        warranty = all_data.get('warranty')
        quantity = all_data.get('quantity')
        if ram<=0 or ram>100:
            raise forms.ValidationError('Laptop RAM must be greater than 0 Gb and less than 100 Gb')
        if rom<=0:
            raise forms.ValidationError('Laptop ROM must be greater than 0 Gb')
        if price<=0:
            raise forms.ValidationError('Laptop Price must be greater than 0 Rs')
        if warranty<=0:
            raise forms.ValidationError('Laptop Warranty must be greater than 0 months')
        if quantity<=0:
            raise forms.ValidationError('Laptop Quantity must at least 1 ')
              

class AccessoriesForm(forms.ModelForm):
    class Meta:
        model = Accessories
        exclude = ['product']
        labels = {
            'product_name':'Product Name',
            'quantity':"Quantity (No's.)",
            'price':'Price (Rs per Quantity)',
            'gimage':'Product Image',
            'warranty':'Expiry (Months)'
        }
        widgets = {
            'product_name':forms.TextInput(attrs={'placeholder':'e.g.Battery,Adapter,KeyBoard'}),
            'price':forms.TextInput(attrs={'placeholder':'e.g. 700'}),
            'quantity':forms.TextInput(attrs={'placeholder':'e.g. 30'}),
            'warranty':forms.TextInput(attrs={'placeholder':'e.g. 6 '}),   
        }

    def clean(self):
        all_data = super().clean()
        price = all_data.get('price')
        warranty = all_data.get('warranty')
        quantity = all_data.get('quantity')
        if price<=0:
            raise forms.ValidationError('Accessories Price must be greater than 0')
        if warranty<=0:
            raise forms.ValidationError('Accessories Warranty must be greater than 0 months')
        if quantity<=0:
            raise forms.ValidationError('Accessories Quantity must at least 1 ')
