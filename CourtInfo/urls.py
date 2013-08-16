from django.conf.urls import patterns, url
from CourtInfo import views

urlpatterns = patterns('',
    
    url(r'^view/(?P<slug>[\w-]+)/$', views.viewCourtInfo, name='viewCourtInfo'),
    url(r'^view/', views.sampleCourtInfo, name='sampleCourtInfo'),
    url(r'^edit/$', views.editCourtInfo, name='editCourtInfo'),
)