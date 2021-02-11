from django.db import models
from django.utils import timezone
import uuid



class MasterPrefecture(models.Model):
    class Meta:
        db_table = 'm_prefecture'

    prefecture_code = models.IntegerField(primary_key=True,editable=False, unique=True)
    prefecture_name = models.CharField(max_length=20)
    prefecture_name_ruby = models.CharField(max_length=50)

    

class MasterCity(models.Model):
    class Meta:
        db_table = 'm_city'
    
    city_code = models.IntegerField(primary_key=True, editable=False, unique=True)
    prefecture_code = models.ForeignKey('MasterPrefecture', to_field='prefecture_code', on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)
    city_name_ruby = models.CharField(max_length=100)


class Shop(models.Model):
    class Meta:
        db_table = 'shop'

    id = models.AutoField(primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=100)
    adress_prefecture = models.ForeignKey('MasterPrefecture', to_field='prefecture_code', on_delete=models.CASCADE)
    adress_city = models.ForeignKey('MasterCity', to_field='city_code', on_delete=models.CASCADE)
    adress_detail = models.CharField(max_length=100)
    nearest_station = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
