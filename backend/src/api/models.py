from django.db import models
from django.utils import timezone
import uuid



class MasterPrefecture(models.Model):
    class Meta:
        db_table = 'm_prefecture'
        verbose_name = '都道府県マスタ'

    prefecture_code = models.IntegerField(primary_key=True,editable=False, unique=True)
    prefecture_name = models.CharField(verbose_name='都道府県名', max_length=20)
    prefecture_name_ruby = models.CharField(verbose_name='都道府県名カナ', max_length=50)

    

class MasterCity(models.Model):
    class Meta:
        db_table = 'm_city'
        verbose_name = '市区町村マスタ'
    
    city_code = models.IntegerField(primary_key=True, editable=False, unique=True)
    prefecture_code = models.ForeignKey('MasterPrefecture', to_field='prefecture_code', on_delete=models.CASCADE)
    city_name = models.CharField(verbose_name='市区町村名', max_length=20)
    city_name_ruby = models.CharField(verbose_name='市区町村名カナ', max_length=50)


class Shop(models.Model):
    class Meta:
        db_table = 'shop'
        verbose_name = '店'

    id = models.IntegerField(primary_key=True, editable=False, unique=True)
    name = models.CharField(verbose_name='店名', max_length=100)
    adress_prefecture = models.ForeignKey('MasterPrefecture', to_field='prefecture_code', on_delete=models.CASCADE)
    adress_city = models.ForeignKey('MasterCity', to_field='city_code', on_delete=models.CASCADE)
    adress_detail = models.CharField(verbose_name='住所詳細', max_length=100)
    nearest_station = models.CharField(verbose_name='最寄駅', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
