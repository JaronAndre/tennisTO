from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'tennisTO.views.home', name='home'),
    url(r'^courts/', include('CourtInfo.urls')),
    url(r'^sign_s3_upload/(?P<court_id>\d+)/$', 'CourtInfo.views.sign_s3', name='sign_s3'),
    url(r'^explore/', include('Explore.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
