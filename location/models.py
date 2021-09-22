import json
from django.db import models

class Location(models.Model):
    device_id = models.CharField(max_length=20, null=False)
    lat = models.CharField(max_length=50, null=False)
    long = models.CharField(max_length=50, null=False)
    vehicle_no = models.CharField(max_length=50, null=False, blank=False, default="")
    hasSent = models.BooleanField(default=False, null=False, blank=False)

    class Meta:
        db_table = 'location'