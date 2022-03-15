from django.urls import path
from .views import Cartview, Customerorderlistview, Customerordersview, Deleteitemview, Accessoriesview, HomeView, Laptopview, Updateallitemview, showlaptop, showAccessories


urlpatterns = [
    path('', HomeView, name='customerhome'),
    path('showlaptop/', showlaptop, name='showlaptop'),
    path('showaccessories/', showAccessories, name='showaccessories'),
    path('customerorderitem/<int:pk>', Laptopview, name='customerlaptopitem'),
    path('customeraccessoriesitem/<int:pk>', Accessoriesview, name='customeraccessoriesitem'),
    path('cartview/', Cartview, name='cartview'),
    path('deleteitem/<int:pk>', Deleteitemview, name='deleteitem'),
    path('customerupdateitem/<int:pk>', Updateallitemview, name='customerupdateitem'),
    path('customerorder/', Customerordersview, name='customerorder'),
    path('customerorderlist/', Customerorderlistview, name='customerorderlist')
]
