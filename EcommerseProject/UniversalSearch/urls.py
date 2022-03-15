from django.urls import path
from .views import *


urlpatterns = [
    path('universalsearch/',Search,name='universalsearch'),
]
