from django.db import models
from django.utils import timezone
import uuid


# class MasterRegions:
#     class Meta:
#         db_name = 'm_regions'
#         verbose_name = '地方マスタ'
    
#     id = models.UUIDField(default=uuid.uuid4, editable=False)
#     name = models.CharField(verbose_name='地方名')


class MasterPrefectures:
    class Meta:
        db_name = 'm_prefectures'
        verbose_name = '都道府県マスタ'

    prefecture_code = models.UUIDField(default=uuid.uuid4, editable=False)
    # region_id = models.ForeignKey(MasterRegions, on_delete=models.CASCADE)
    prefecture_name = models.CharField(verbose_name='都道府県名')
    prefecture_name_ruby = models.CharField(verbose_name='都道府県名カナ')

    

class MasterCities:
    class Meta:
        db_name = 'm_cities'
        verbose_name = '市区町村マスタ'
    
    city_code = models.UUIDField(default=uuid.uuid4, editable=False)
    # region_id = models.ForeignKey(MasterRegions, on_delete=models.CASCADE)
    prefecture_code = models.ForeignKey(MasterPrefectures, on_delete=models.CASCADE)
    city_name = models.CharField(verbose_name='市区町村名')
    city_name_ruby = models.CharField(verbose_name='市区町村名カナ')


class Shops(models.Model):
    class Meta:
        db_table = 'shops'
        verbose_name = 'shops'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='店名')
    adress_prefecture = models.ForeignKey(MasterPrefectures, on_delete=models.CASCADE)
    adress_city = models.ForeignKey(MasterCities, on_delete=models.CASCADE)
    adress_detail = models.CharField(verbose_name='住所詳細')