from rest_framework import serializers
from items.models import Item

class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields=['id','name']
        detail = serializers.HyperlinkedRelatedField(
            queryset=Item.objects.all(),
            view_name='api-detial'
        )

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields=['id','name', 'description', 'image']