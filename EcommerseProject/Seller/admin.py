from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'seller', 'category_name']
admin.site.register(Product, ProductAdmin)


class LaptopAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'brand_name', 'model_name', 'ram', 'rom', 'processor', 'price', 'warranty', 'limage']
admin.site.register(Laptop, LaptopAdmin)


class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ['product', 'product_name', 'quantity', 'price', 'gimage']
admin.site.register(Accessories, AccessoriesAdmin)


