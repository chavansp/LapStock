from .models import Custorders
from django import forms


class Ordersform(forms.ModelForm):
    class Meta:
        model = Custorders
        fields = '__all__'
        exclude = ['customer', 'laptop', 'accessories', 'price', 'items']
