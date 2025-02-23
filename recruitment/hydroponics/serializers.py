from rest_framework import serializers
from hydroponics.models import HydroponicSystem, Measurement

class HydroponicSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydroponicSystem
        fields = ['id', 'owner', 'name', 'description', 'created_at', 'updated_at']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'hydroponic_system', 'ph', 'temperature', 'tds', 'timestamp']
