from django.db import models

# Create your models here.

class WeatherData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    precipitation = models.FloatField()
    cloud_cover = models.CharField(max_length=50)
    atmospheric_pressure = models.FloatField()
    uv_index = models.IntegerField()
    season = models.CharField(max_length=50)
    visibility = models.FloatField()

    def __str__(self):
        return f"WeatherData({self.temperature}, {self.humidity}, {self.wind_speed}, {self.precipitation}, {self.cloud_cover}, {self.atmospheric_pressure}, {self.uv_index}, {self.season}, {self.visibility})"
