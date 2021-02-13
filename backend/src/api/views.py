from rest_framework import viewsets, filters, generics
from .models import Shop, MasterPrefecture, MasterCity
from .serializers import ShopListSerializer, ShopDetailSerializer, MasterPrefectureSerializer, MasterCitySerializer 


class MasterPrefectureApiView(generics.ListCreateAPIView):
    queryset = MasterPrefecture.objects.all()
    serializer_class = MasterPrefectureSerializer

class MasterCityApiView(generics.ListCreateAPIView):
    queryset = MasterCity.objects.all()
    serializer_class = MasterCitySerializer

class ShopListApiView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopListSerializer

class ShopDetailApiView(generics.RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopDetailSerializer