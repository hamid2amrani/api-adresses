from django.db import models


class Address(models.Model):
    label = models.CharField(max_length=255)
    housenumber = models.CharField(max_length=20)
    street = models.CharField(max_length=255)
    postcode = models.CharField(max_length=10)
    citycode = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()


