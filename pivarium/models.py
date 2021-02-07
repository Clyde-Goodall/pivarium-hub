from django.db import models
from colorful.fields import RGBColorField

#globals


#models
class Sensor(models.Model):

    class Meta():
        verbose_name_plural = "Sensors"
    
    sensor_type = models.CharField(max_length=10)
    unit = models.CharField(max_length=5)

    def __str__(self):
        return self.sensor_type


class Station(models.Model):

    class Meta():
        verbose_name_plural = "Stations"
    
    title = models.CharField(max_length=20, default="Raspberry Pi")
    sid = models.CharField(max_length=15, default="None")
    color = RGBColorField(default='#FF0000')
    desc = models.TextField(default="Data channel source")
    def __str__(self):
        return self.title


class StationData(models.Model):

    class Meta():
        verbose_name_plural = "Station Data"
    
    sid = models.CharField(max_length=15, default="None")#refers to Station
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True) # handled autpomatically
    sensor_type = models.CharField(max_length=15, default="unknown")
    station = models.ForeignKey(Station, on_delete=models.CASCADE, default=0)
   
    def __str__(self):
        return self.value

class ClientSettings(models.Model):

    poll_time = models.IntegerField(default=10)

