from rest_framework import serializers
from .models import Shop

class ShopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'adress_prefecture', 'adress_city', 'nearest_station']


class ShopDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'adress_prefecture', 'adress_city', 'nearest_station']

