from rest_framework import viewsets, filters, generics
from .models import Shop
from .serializers import ShopListSerializer, ShopDetailSerializer


class ShopListApiView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopListSerializer

class ShopDetailApiView(generics.RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopDetailSerializer