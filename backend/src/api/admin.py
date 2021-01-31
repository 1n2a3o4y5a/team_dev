from django.contrib import admin
from .models import MasterPrefecture, MasterCity, Shop

class ApiAdmin(admin.ModelAdmin):
    pass


admin.site.register(MasterPrefecture)
admin.site.register(MasterCity)
admin.site.register(Shop)
