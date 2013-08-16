from django.db import models


class Court(models.Model):
    photosynth_url = models.URLField()
    
    map_url = models.URLField()
    larger_map_url = models.URLField()
    get_directions_url = models.URLField()
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    court_info = models.TextField(blank=True)
    court_condition = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name
    
    def court_info_html(self):
        return self.court_info.replace('\n', '<br>')
        
    def court_condition_html(self):
        return self.court_condition.replace('\n', '<br>')
        
    
class ThingsNearby(models.Model):
    court = models.ForeignKey(Court)
    text = models.CharField(max_length=200)
    url = models.URLField(blank=True)

    def __unicode__(self):
        return self.text