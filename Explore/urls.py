from django.conf.urls import patterns, url
from Explore import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)