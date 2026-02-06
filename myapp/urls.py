from django.urls import path
from .views import ItemDelete, ItemUpdate, ItemCreate, ItemRetrieve, ItemList

urlpatterns = [
    path('itemslist', ItemList.as_view(),name='itemslist'),
    path('itemcreate', ItemCreate.as_view(), name='item-create'),
    path('updateitem/<int:pk>', ItemUpdate.as_view(), name='item-detail'),
    path('deleteitem/<int:pk>', ItemDelete.as_view(), name='item-delete'), 
    path('retrieveitem/<int:pk>', ItemRetrieve.as_view(), name='item-retrieve'),
]
