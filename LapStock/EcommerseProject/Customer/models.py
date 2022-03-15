from django.db import models
from Accounts.models import Customer,CustomUser
from Seller.models import Laptop,Accessories
from CustomerProfile.models import Address


class Order_item(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, null=True)
    accessories = models.ForeignKey(Accessories, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.customer.name}'


class Custorders(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    mobile_no = models.BigIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, null=True)
    accessories = models.ForeignKey(Accessories, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
    items = models.IntegerField()

    def __str__(self):
        return f'{self.customer.name}'
