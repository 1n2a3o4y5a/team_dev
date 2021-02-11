from rest_framework import viewsets, filters
from .models import Shop
from .serializers import ShopSeriarizer


class ShopView(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSeriarizer