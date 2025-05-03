from django.urls import path
from .views import ItemDetail, ItemListCreate

urlpatterns = [
    path('items/', ItemListCreate.as_view(), name='item-list-create'),
    path('items/<int:pk>', ItemDetail.as_view(), name='item-detail'),   
]
