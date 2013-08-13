from django.shortcuts import render

def index(request): 
    return render(request, 'CourtInfo/court_info.html',  )
