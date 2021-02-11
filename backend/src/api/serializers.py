from rest_framework import serializers
from .models import Shop

class ShopSeriarizer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'adress_prefecture', 'adress_city', 'nearest_station']