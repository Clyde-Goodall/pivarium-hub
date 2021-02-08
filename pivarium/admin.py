from django.contrib import admin
from pivarium.models import Station, StationData, Sensor, ClientSettings

#all models being registered
admin.site.register(Station)
admin.site.register(StationData)
admin.site.register(Sensor)
admin.site.register(ClientSettings)