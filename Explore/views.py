from django.http import HttpResponse
from django.shortcuts import render


def index(request): 
    courts = Court.objects.all()
    cities = {}
    for court in courts:
        if cities[court.city] == undefined:
            cities[court.city] = [court]
        else:
            cities[court.city].add(court)
    
    context = {'is_explore_page': True}
    return render(request, 'Explore/explore_main.html', context)