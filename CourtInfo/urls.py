from django.conf.urls import patterns, url
from CourtInfo import views

urlpatterns = patterns('',
    url(r'^view/(?P<slug>[\w-]+)/$', views.viewCourtInfo, name='viewCourtInfo'),
    url(r'^view/', views.viewCourtInfoBase, name='viewCourtInfoBase'),
    url(r'^edit/$', views.editCourtInfo, name='editCourtInfo'),
    url(r'^markers_list/$', views.getCourtMarkersJSON, name='getCourtMarkersJSON'),
    url(r'^markers_list_json/$', views.getCourtMarkersJSON, name='getCourtMarkersJSON2'),
)