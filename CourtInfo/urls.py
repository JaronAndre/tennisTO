from django.conf.urls import patterns, url
from CourtInfo import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
