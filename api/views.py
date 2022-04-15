from django.shortcuts import render
<<<<<<< HEAD
from requests import request
=======
>>>>>>> e0015007c475aec69c5e1b13c18609d87a575b4a
from rest_framework.generics import  RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .serializers import ItemDetailSerializer, ItemListSerializer
from items.models import Item
from rest_framework.filters import SearchFilter, OrderingFilter
<<<<<<< HEAD
from .permissions import IsAdminOrReadOnly, IsAdminOrOwnerCanView
=======
>>>>>>> e0015007c475aec69c5e1b13c18609d87a575b4a

class ItemDetialView(RetrieveUpdateDestroyAPIView):
    queryset=Item.objects.all()
    serializer_class=ItemDetailSerializer
<<<<<<< HEAD
    permission_classes=[IsAdminOrOwnerCanView]

=======
>>>>>>> e0015007c475aec69c5e1b13c18609d87a575b4a

class ItemListView(ListCreateAPIView):
    queryset=Item.objects.all()
    serializer_class=ItemListSerializer
<<<<<<< HEAD
    permission_classes=[IsAdminOrReadOnly]
    def get_serializer_context(self):
        return {'request':self.request}
        
=======
>>>>>>> e0015007c475aec69c5e1b13c18609d87a575b4a
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['description', 'name']