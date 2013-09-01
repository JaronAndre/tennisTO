from django.db import models
from geoposition.fields import GeopositionField
import os
import uuid


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

        
SURFACE_TYPE_CHOICES = (
    (0, ''),
    (1, 'Acrylic'),
    (2, 'Artificial clay'),
    (3, 'Artificial grass'),
    (4, 'Asphalt'),
    (5, 'Carpet'),
    (6, 'Clay'),
    (7, 'Concrete'),
    (8, 'Grass'),
)
    
class Court(models.Model):
    name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=150, blank=True)
    city = models.ForeignKey(City)
    geo_position = GeopositionField()
    
    slug = models.SlugField(unique=True)
    
    photosynth_url = models.URLField(blank=True)
    fallback_image_url = models.URLField(blank=True)
    
    is_public = models.BooleanField(default=True)
    number_of_courts = models.IntegerField(default=2, blank=True)
    has_lights = models.BooleanField(default=True)
    has_public_washroom = models.NullBooleanField()
    surface_type = models.IntegerField(default=4, choices=SURFACE_TYPE_CHOICES)
    court_info = models.TextField(blank=True)
    court_condition = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
    
    def court_info_html(self):
        return self.court_info.replace('\n', '<br>')
        
    def court_condition_html(self):
        return self.court_condition.replace('\n', '<br>')
        
    def full_address(self):
        cityName = self.city.name
        provinceName = self.city.province.name
        if self.street_address:
            return '{0}, {1}'.format(self.street_address, self.city.full_address())
        else:
            return '{0}, {1}'.format(self.name, self.city.full_address())
    
    def surface_type_string(self):
        return SURFACE_TYPE_CHOICES[self.surface_type][1]
    
    class Meta:
        verbose_name = 'court'
        verbose_name_plural = 'courts'
        

class ThingsNearby(models.Model):
    court = models.ForeignKey(Court)
    text = models.CharField(max_length=200)
    url = models.URLField(blank=True)

    def __unicode__(self):
        return self.text
        

class CourtPhoto(models.Model):
    court = models.ForeignKey(Court)
    caption = models.CharField(max_length=200, blank=True)
    image_url = models.URLField(blank=True)
    time_added = models.DateTimeField(auto_now=True)
    is_validated = models.BooleanField(default=False)
    
    @staticmethod
    def create_unique_path_name(court):
        # Add a special path if we're testing on a dev machine 
        # instead of the live server
        path = os.environ.get('S3_LOCAL_TEST_PATH')
        if path:
            path = path + str(court.pk) + '/images/'
        else:
            path = str(court.pk) + '/images/'
    
        return path + uuid.uuid4().hex
        
    def __unicode__(self):
        return self.image_url