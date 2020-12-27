from django.db import models
from django.utils import timezone

class Shops(models.Model):
    class Meta:
        db_table = 'shops'
        verbose_name = 'shops'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='店名')
    address_prefecture = models.CharField(verbose_name='都道府県名')
    adress_city = models.CharField(verbose_name='市区町村名')
    adress_detail = models.CharField(verbose_name='住所詳細')
    nearest_station = models.CharField(verbose_name='最寄駅')
    about_time_walk = models.CharField(verbose_name='駅徒歩時間')
    review = models.IntegerField(vervose_name='レビュー')
    
    