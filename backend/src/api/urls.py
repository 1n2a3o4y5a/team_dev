from django.urls import path, include
from rest_framework import routers
from . import views




urlpatterns = [
    path('shop/', views.ShopListApiView.as_view()),
    path('shop/detail/<int:pk>', views.ShopDetailApiView.as_view())
]