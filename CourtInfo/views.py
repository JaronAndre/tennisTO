from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from CourtInfo.models import Court
from CourtInfo.forms import CourtInfoForm

def viewCourtInfoBase(request):
    return render(request, 'CourtInfo/court_info.html',  )

def viewCourtInfo(request, slug):
    try:
        court = Court.objects.get(slug = slug)
    except Court.DoesNotExist:
        raise Http404
        
    context = {'court': court}
    return render(request, 'CourtInfo/court_info_view.html', context)

    
def editCourtInfo(request, slug):
    try:
        court = Court.objects.get(slug = slug)
    except Court.DoesNotExist:
        raise Http404
    
    if request.method == 'POST':
        form = CourtInfoForm(request.POST)
        if form.is_valid():
            # Need to handle this 
            pass
    else:
        initial = {
            'name': court.name,
            
            'street_address': court.street_address,
            'city': court.city,
            'geo_position': court.geo_position,
            
            'is_public': court.is_public,
            'number_of_courts': court.number_of_courts,
            'has_lights': court.has_lights,
            'has_public_washroom': court.has_public_washroom,
            'surface_type': court.surface_type,
            'court_info': court.court_info,
            'court_condition': court.court_condition,
        }
        form = CourtInfoForm(initial=initial)
        
        context = {
            'form': form,
            'court': court,
        }
    return render(request, 'CourtInfo/court_info_edit.html', context)  
    

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