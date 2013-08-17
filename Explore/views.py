from django.http import HttpResponse
from django.shortcuts import render


def index(request): 
    context = {'is_explore_page': True}
    return render(request, 'Explore/explore_main.html', context)