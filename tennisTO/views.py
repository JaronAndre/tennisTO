from django.shortcuts import render
from django.http import HttpResponse
from CourtInfo.models import Court

def home(request):
    context = {'is_homepage': True}
    return render(request, 'homepage.html', context)
    