from django.shortcuts import render
from django.http import HttpResponse
from CourtInfo.models import Court

def sampleCourtInfo(request):
    return render(request, 'CourtInfo/court_info.html',  )
   
   
def viewCourtInfo(request, slug):
    try:
        court = Court.objects.get(slug = slug)
    except Court.DoesNotExist:
        raise Http404
        
    context = {'court': court}
    return render(request, 'CourtInfo/court_info_view.html', context)

    
def editCourtInfo(request): 
    return HttpResponse("Need to implement CourtInfo.editCourtInfo")
