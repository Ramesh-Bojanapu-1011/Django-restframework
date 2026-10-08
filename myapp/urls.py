from django.urls import path

from .views import ItemCreate, ItemDelete, ItemList, ItemRetrieve, ItemUpdate

urlpatterns = [
    path("itemslist", ItemList.as_view(), name="itemslist"),
    path("itemcreate", ItemCreate.as_view(), name="item-create"),
    path("updateitem/<int:pk>", ItemUpdate.as_view(), name="item-detail"),
    path("deleteitem/<int:pk>", ItemDelete.as_view(), name="item-delete"),
    path("retrieveitem/<int:pk>", ItemRetrieve.as_view(), name="item-retrieve"),
]
