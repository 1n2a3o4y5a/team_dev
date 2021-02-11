from django.urls import path
from . import views
from rest_framework import routers
from . import serializers

# urlpatterns = [
#     path('shops/', views.ShopView)
# ]

router = routers.DefaultRouter()
router.register(r'shops', views.ShopView)
