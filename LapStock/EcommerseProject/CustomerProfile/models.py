from django.db import models
from Customer.models import Customer


class Country(models.Model):
    country_name = models.CharField(max_length=32)

    def __str__(self):
        return self.country_name


class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    state_name = models.CharField(max_length=32)

    def __str__(self):
        return self.state_name


class City(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    city_name = models.CharField(max_length=32)


    def __str__(self):
        return self.city_name


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100, default=None)
    mobile = models.BigIntegerField(default=None)
    country = models.CharField(max_length=50)
    state =models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=500, default=None)
    address_type = models.CharField(max_length=20, default=None)

    def __str__(self):
        return f'{self.address}'

