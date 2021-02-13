from rest_framework import serializers
from .models import Shop, Review, MasterPrefecture, MasterCity

class MasterPrefectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterPrefecture
        fields = '__all__'

class MasterCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterCity
        fields = '__all__'

class ShopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'adress_prefecture', 'adress_city', 'nearest_station']

class ShopDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'