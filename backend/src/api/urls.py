from django.urls import path, include
from rest_framework import routers
from . import views




urlpatterns = [
    path('master/prefecture/', views.MasterPrefectureApiView.as_view()),
    path('master/city/', views.MasterCityApiView.as_view()),
    path('shop/', views.ShopListApiView.as_view()),
    path('shop/detail/<int:pk>', views.ShopDetailApiView.as_view())
]