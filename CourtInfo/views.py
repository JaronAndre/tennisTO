from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from CourtInfo.models import Court
from CourtInfo.forms import CourtInfoForm
import time, os, json, base64, hmac, sha, urllib

def viewCourtInfoBase(request):
    return HttpResponse('CourtInfo.viewCourtInfoBase')

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
    
    context = {}
    if request.method == 'POST':
        form = CourtInfoForm(request.POST)
        if form.is_valid():
            
            court.name = form.cleaned_data['name']
            
            court.street_address = form.cleaned_data['street_address']
            court.city = form.cleaned_data['city']
            court.geo_position = form.cleaned_data['geo_position']
            
            court.is_public = form.cleaned_data['is_public']
            
            court.number_of_courts = form.cleaned_data['number_of_courts']
            court.has_lights = form.cleaned_data['has_lights']
            court.has_public_washroom = form.cleaned_data['has_public_washroom']
            court.surface_type = form.cleaned_data['surface_type']
            court.court_info = form.cleaned_data['court_info']
            court.court_condition = form.cleaned_data['court_condition']
            court.save()
            
            return HttpResponseRedirect('/courts/view/' + slug + '/') # Redirect after POST
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

    context['court'] = court
    context['form'] = form
    return render(request, 'CourtInfo/court_info_edit.html', context)  
    

def sign_s3(request):
    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')       
    AWS_SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    S3_BUCKET = os.environ.get('S3_BUCKET')

    object_name = request.GET['s3_object_name']
    mime_type = request.GET['s3_object_type']

    expires = int(time.time()+10)
    amz_headers = "x-amz-acl:public-read"

    put_request = "PUT\n\n%s\n%d\n%s\n/%s/%s" % (mime_type, expires, amz_headers, S3_BUCKET, object_name)

    signature = base64.encodestring(hmac.new(AWS_SECRET_KEY,put_request, sha).digest())
    signature = urllib.quote_plus(signature.strip())

    url = 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, object_name)

    return HttpResponse(json.dumps({
        'signed_request': '%s?AWSAccessKeyId=%s&Expires=%d&Signature=%s' % (url, AWS_ACCESS_KEY, expires, signature),
         'url': url
    })) 


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