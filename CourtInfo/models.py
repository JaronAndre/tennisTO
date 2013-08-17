from django.db import models
from geoposition.fields import GeopositionField


class Court(models.Model):
    photosynth_url = models.URLField()
    
    geo_position = GeopositionField()
    
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, default='Richmond Hill')
    province = models.CharField(max_length=100, default='Ontario')
    country = models.CharField(max_length=100, default='Canada')
    
    is_public = models.BooleanField(default=True)
    
    slug = models.SlugField(unique=True)
    
    court_info = models.TextField(blank=True)
    court_condition = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
    
    def court_info_html(self):
        return self.court_info.replace('\n', '<br>')
        
    def court_condition_html(self):
        return self.court_condition.replace('\n', '<br>')
        
    def full_address(self):
        if self.address:
            return '{0}, {1}, {2}, {3}'.format(self.address, self.city, self.province, self.country)
        else:
            return '{0}, {1}, {2}, {3}'.format(self.name, self.city, self.province, self.country)
        
    
class ThingsNearby(models.Model):
    court = models.ForeignKey(Court)
    text = models.CharField(max_length=200)
    url = models.URLField(blank=True)

    def __unicode__(self):
        return self.text