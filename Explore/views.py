from django.http import HttpResponse
from django.shortcuts import render
from CourtInfo.models import Court, City


def index(request):
    courts = Court.objects.all()
       
    # Group the courts into cities
    cities = City.objects.all().order_by('name')
    
    context = {
        'is_explore_page': True,
        'cities': cities
    }
    return render(request, 'Explore/explore_main.html', context)

