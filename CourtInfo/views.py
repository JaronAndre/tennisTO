from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from CourtInfo.models import Court

def viewCourtInfoBase(request):
    return render(request, 'CourtInfo/court_info.html',  )

def viewCourtInfo(request, slug):
    try:
        court = Court.objects.get(slug = slug)
    except Court.DoesNotExist:
        raise Http404
        
    context = {'court': court}
    return render(request, 'CourtInfo/court_info_view.html', context)


def getCourtMarkersJSON(request):
    courts = Court.objects.all()
    fields = ('name', 'geo_position', 'slug')
    data = serializers.serialize("json", courts, fields = fields)
    return HttpResponse(data, content_type="application/json")
    

def getCourtMarkersJSON2(request):
    courts = Court.objects.all()
    data = serializers.serialize("json", courts)
    return HttpResponse(data)
    

def getCourtsInCity(request, city):
    courts = Court.objects.filter(city = city)
    fields = ('name', 'slug', 'is_public')
    data = serializers.serialize("json", courts, fields = fields)
    return HttpResponse(data, content_type="application/json")