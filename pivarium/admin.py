from django.contrib import admin
from pivarium.models import Station, StationData, Sensor

# Register your models here.
admin.site.register(Station)
admin.site.register(StationData)
admin.site.register(Sensor)