from django.urls import path
from .views import ProductView, Selleraccessoriesdeleteview, Selleraccessoriesupdateview, Selleraccessoriesview, Sellerhomeview, Sellerinventoryview, Sellerlaptopdeleteview, Sellerlaptopupdateview, Sellerlaptopview


urlpatterns = [
    path('sellerhome/', Sellerhomeview, name='sellerhome'),
    path('sellerproduct/', ProductView, name='sellerproduct'),
    path('sellerlaptop/', Sellerlaptopview, name='sellerlaptop'),
    path('selleraccessories/', Selleraccessoriesview, name='selleraccessories'),
    path('sellerinventory/', Sellerinventoryview, name='sellerinventory'),
    path('sellerlaptopupdate/<int:lapupdate>', Sellerlaptopupdateview, name='sellerlaptopupdate'),
    path('selleraccessoriesupdate/<int:groupdate>', Selleraccessoriesupdateview, name='selleraccessoriesupdate'),
    path('sellerlaptopdelete/<int:lapdelete>', Sellerlaptopdeleteview, name='sellerlaptopdelete'),
    path('selleraccessoriesdelete/<int:grodelete>', Selleraccessoriesdeleteview, name='selleraccessoriesdelete'),
]
