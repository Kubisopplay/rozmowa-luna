from django.contrib.auth.models import User
from django.db import models

class HydroponicSystem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='hydroponic_systems')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Measurement(models.Model):
    hydroponic_system = models.ForeignKey(HydroponicSystem, on_delete=models.CASCADE, related_name='measurements')
    ph = models.DecimalField(max_digits=4, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    tds = models.DecimalField(max_digits=6, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
