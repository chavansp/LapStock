import django_filters
from Seller.models import Laptop, Accessories
from django import forms


class LaptopFilter(django_filters.FilterSet):
    # price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    # price=django_filters.NumberFilter(lookup_expr='lte')
    # max_price=django_filters.NumberFilter(name='price',lookup_expr='lte')
    class Meta:
        model = Laptop
        fields = '__all__'
        exclude = ['limage', 'seller', 'stock', 'warranty', 'price', 'product']


class AccessoriesFilter(django_filters.FilterSet):
    # price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    # price=django_filters.NumberFilter(lookup_expr='lte')
    # max_price=django_filters.NumberFilter(name='price',lookup_expr='lte')
    class Meta:
        model = Accessories
        fields = '__all__'
        exclude = ['gimage', 'seller', 'stock', 'warranty', 'price', 'product']
