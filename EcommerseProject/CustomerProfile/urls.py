from django.urls import path
from .views import CustomerAddressUpdateView, CustomerAddressview, deleteProfile, load_states, load_cities, showProfile


urlpatterns = [
    path('customeradd/', CustomerAddressview, name='customeraddress'),
    path('ajax/load-states/', load_states, name='ajax_load_states'),
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),
    path('showProfile/', showProfile, name='showProfile'),
    # path('update_Profile/<int:pk>', update_Profile, name='update_Profile'),
    path('delete_Profile/<int:pk>', deleteProfile, name='delete_Profile'),
    path('customeraddupdate/<int:pk>', CustomerAddressUpdateView.as_view(), name='customeraddressupdate'),
]
