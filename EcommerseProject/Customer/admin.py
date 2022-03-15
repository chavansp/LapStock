from django.contrib import admin
from .models import Order_item,Custorders


class OrderAdmin(admin.ModelAdmin):
    list_display=['id', 'customer', 'laptop', 'price', 'quantity']
admin.site.register(Order_item, OrderAdmin)

class CustOrderitemsAdmin(admin.ModelAdmin):
    list_display=['id', 'date', 'customer', 'laptop', 'accessories', 'price', 'items', 'address', 'fname', 'lname', 'mobile_no']
admin.site.register(Custorders, CustOrderitemsAdmin)
