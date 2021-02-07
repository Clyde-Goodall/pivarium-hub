from django.shortcuts import render
from django.http import HttpResponse
from pivarium.models import Station, StationData
# Create your views here.

def home(request):
    return render(
        request = request,
        template_name="frontpage/index.html",
        context = {'stations' : Station.objects.all}
    )

def station(request, sid):
    return render(
        request = request,
        template_name="frontpage/station.html",
        context= {
            'current_station' : Station.objects.filter(sid=sid),
            'stations': Station.objects.all}
    )
    