from django.contrib import admin
from hydroponics.models import HydroponicSystem, Measurement

@admin.register(HydroponicSystem)
class HydroponicSystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('hydroponic_system', 'ph', 'temperature', 'tds', 'timestamp')
    search_fields = ('ph', 'temperature', 'tds')
    list_filter = ('timestamp', 'ph', 'temperature', 'tds')