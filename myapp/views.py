from rest_framework import generics
from rest_framework import filters
from .models import Item
from .serializers import ItemSerializer


# Create your views here.
class ItemCreate(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemUpdate(generics.UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDelete(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemRetrieve(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemList(generics.ListAPIView):
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    filterset_fields = ["name", "description"]
    ordering_fields = ["name", "description"]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
