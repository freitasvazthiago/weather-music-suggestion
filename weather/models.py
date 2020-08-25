from django.db import models

class Weather(models.Model):
    city_id = models.IntegerField()
    city_name = models.CharField(max_length=200)