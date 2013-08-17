from django.shortcuts import render
from django.http import HttpResponse
from CourtInfo.models import Court

def home(request):
    context = {}
    return render(request, 'homepage.html', context)
    