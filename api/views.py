from django.shortcuts import render
from rest_framework.generics import  RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .serializers import ItemDetailSerializer, ItemListSerializer
from items.models import Item
from rest_framework.filters import SearchFilter, OrderingFilter

class ItemDetialView(RetrieveUpdateDestroyAPIView):
    queryset=Item.objects.all()
    serializer_class=ItemDetailSerializer

class ItemListView(ListCreateAPIView):
    queryset=Item.objects.all()
    serializer_class=ItemListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['description', 'name']