from django.db import models
from django.utils import timezone
import uuid



class MasterPrefectures(models.Model):
    class Meta:
        db_table = 'm_prefectures'
        verbose_name = '都道府県マスタ'

    prefecture_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    prefecture_name = models.CharField(verbose_name='都道府県名', max_length=20)
    prefecture_name_ruby = models.CharField(verbose_name='都道府県名カナ', max_length=50)

    

class MasterCities(models.Model):
    class Meta:
        db_table = 'm_cities'
        verbose_name = '市区町村マスタ'
    
    city_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    prefecture_code = models.ForeignKey('MasterPrefectures', to_field='prefecture_code', on_delete=models.CASCADE)
    city_name = models.CharField(verbose_name='市区町村名', max_length=20)
    city_name_ruby = models.CharField(verbose_name='市区町村名カナ', max_length=50)


class Shops(models.Model):
    class Meta:
        db_table = 'shops'
        verbose_name = 'shops'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(verbose_name='店名', max_length=50)
    adress_prefecture = models.ForeignKey('MasterPrefectures', to_field='prefecture_code', on_delete=models.CASCADE)
    adress_city = models.ForeignKey('MasterCities', to_field='city_code', on_delete=models.CASCADE)
    adress_detail = models.CharField(verbose_name='住所詳細', max_length=50)