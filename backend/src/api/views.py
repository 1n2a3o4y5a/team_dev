from rest_framework import viewsets, filters, generics
from .models import Shop
from .serializers import ShopSeriarizer


class ShopView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSeriarizer