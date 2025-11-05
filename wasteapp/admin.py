from django.contrib import admin
from .models import Bin, CollectionTruck, CollectionLog

@admin.register(Bin)
class BinAdmin(admin.ModelAdmin):
    list_display = ('name','location','fill_percent','status','last_reported_at')
    list_filter = ('status',)

@admin.register(CollectionTruck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ('name','driver_name','capacity','active')

@admin.register(CollectionLog)
class LogAdmin(admin.ModelAdmin):
    list_display = ('bin','truck','collected_at')
    list_filter = ('collected_at',)
