from django.urls import path

from Show.views import *
from Warehouse.views import *
urlpatterns = [
    path('',product_1),
    path('product_1',product_1),
    path('product_2',product_2),
    path('product_3',product_3),
    path('product_4',product_4),
    path('product_5',product_5),
    path('refresh',refresh),
]