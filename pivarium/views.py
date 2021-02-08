from django.shortcuts import render
from django.http import HttpResponse
from pivarium.models import Station, StationData

#home view, with all stations? Layout still up in the air.
def home(request):
    
    return render(
        request = request,
        template_name="frontpage/index.html",
        context = {'stations' : Station.objects.all}
    )

#view individual stations using mac address hex as identifier
def station(request, sid):
    return render(
        request = request,
        template_name="frontpage/station.html",
        context= {
            'current_station' : Station.objects.filter(sid=sid)[0],
            'stations': Station.objects.all
            }
    )
    