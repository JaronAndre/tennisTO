from django.db import models
from geoposition.fields import GeopositionField


class Country(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'
        
        
class Province(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10, blank=True)
    country = models.ForeignKey(Country)
    def __unicode__(self):
        return self.name
    def full_address(self):
        if self.short_name:
            return '{0}, {1}'.format(self.short_name, self.country.name)
        else:
            return '{0}, {1}'.format(self.name, self.country.name)
    class Meta:
        verbose_name = 'province'
        verbose_name_plural = 'provinces'


class City(models.Model):
    name = models.CharField(max_length=100)
    province = models.ForeignKey(Province)
    def __unicode__(self):
        return self.full_address()
    def full_address(self):
        return '{0}, {1}'.format(self.name, self.province.full_address())
    def sorted_courts(self):
        return self.court_set.order_by('name')
    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'


class Court(models.Model):
    name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=150, blank=True)
    city = models.ForeignKey(City)
    geo_position = GeopositionField()
    
    slug = models.SlugField(unique=True)
    
    photosynth_url = models.URLField(blank=True)
    fallback_image_url = models.URLField(blank=True)
    
    is_public = models.BooleanField(default=True)
    court_info = models.TextField(blank=True)
    court_condition = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
    
    def court_info_html(self):
        return self.court_info.replace('\n', '<br>')
        
    def court_condition_html(self):
        return self.court_condition.replace('\n', '<br>')
        
    def full_address(self):
        cityName = self.city.name;
        provinceName = self.city.province.name;
        if self.street_address:
            return '{0}, {1}'.format(self.street_address, self.city.full_address())
        else:
            return '{0}, {1}'.format(self.name, self.city.full_address())
    
    class Meta:
        verbose_name = 'court'
        verbose_name_plural = 'courts'
        

class ThingsNearby(models.Model):
    court = models.ForeignKey(Court)
    text = models.CharField(max_length=200)
    url = models.URLField(blank=True)

    def __unicode__(self):
        return self.text