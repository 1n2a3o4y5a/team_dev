from rest_framework import serializers
from .models import Shop

class ShopSeriarizer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name']