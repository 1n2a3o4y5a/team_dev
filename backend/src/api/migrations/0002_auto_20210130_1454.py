# Generated by Django 3.1.5 on 2021-01-30 05:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shops',
            options={'verbose_name': 'shop'},
        ),
        migrations.AddField(
            model_name='shops',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shops',
            name='nearest_station',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='最寄駅'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shops',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='shops',
            name='adress_detail',
            field=models.CharField(max_length=100, verbose_name='住所詳細'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='name',
            field=models.CharField(max_length=100, verbose_name='店名'),
        ),
        migrations.AlterModelTable(
            name='mastercities',
            table='m_city',
        ),
        migrations.AlterModelTable(
            name='masterprefectures',
            table='m_prefecture',
        ),
        migrations.AlterModelTable(
            name='shops',
            table='shop',
        ),
    ]
