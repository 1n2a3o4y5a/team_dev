from django.db import models
from django.utils import timezone


class MasterRegions:
    class Meta:
        db_name = 'm_regions'
        verbose_name = '地方マスタ'
    
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='地方名')


class MasterPrefectures:
    class Meta:
        db_name = 'm_prefectures'
        verbose_name = '都道府県マスタ'

    id = models.UUIDField(default=uuid.uuid4, editable=False)
    region_id = models.ForeignKey(MasterRegions, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='都道府県名')
    

class MasterCities:
    class Meta:
        db_name = 'm_cities'
        verbose_name = '市区町村マスタ'
    
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    region_id = models.ForeignKey(MasterRegions, on_delete=models.CASCADE)
    prefecture_id = models.ForeignKey(MasterPrefectures, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='市区町村名')


class Shops(models.Model):
    class Meta:
        db_table = 'shops'
        verbose_name = 'shops'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='店名')