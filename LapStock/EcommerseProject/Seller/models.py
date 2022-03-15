from django.db import models
from Accounts.models import Seller


category_choices = [('laptop', 'laptop'), ('accessories', 'accessories')]

class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100, choices=category_choices)

    def __str__(self):
        return f'{self.seller}//{self.category_name}'


class Laptop(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    ram = models.IntegerField()
    rom = models.IntegerField()
    processor = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)
    warranty = models.IntegerField()
    limage = models.ImageField(upload_to='Laptops/')

    def __str__(self):
        return f'{self.brand_name}//{self.model_name}'

    def __str__(self):
        return f'{self.brand_name}//{self.model_name}'


class Accessories(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    warranty = models.IntegerField()
    gimage = models.ImageField(upload_to='Accessories/')

    def __str__(self):
        return self.product_name
