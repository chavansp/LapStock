from django.urls import path
from .views import CustomerRazorpayPayment, CustomerRazorpayconfirm, report


urlpatterns = [
    path('customerpay/', CustomerRazorpayPayment, name='customerrazorpay'),
    path('customersuccess/', CustomerRazorpayconfirm, name='customerrazorpaysuccess'),
    path('report/<int:id>', report, name='report')
]