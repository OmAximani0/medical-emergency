from django.db import models

class Location(models.Model):
    device_id = models.CharField(max_length=20, null=False)
    lat = models.CharField(max_length=50, null=False)
    long = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'location'