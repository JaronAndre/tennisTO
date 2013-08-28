from django import forms
from CourtInfo.models import City, Court, SURFACE_TYPE_CHOICES
from geoposition.forms import GeopositionField


NUMBER_OF_COURT_CHOICES = [
    ('1','1'), 
    ('2','2'),
    ('3','3'),
    ('4','4'), 
    ('5','5'),
    ('6','6'), 
    ('7','7'), 
    ('8','8'),
    ('9','9'), 
    ('10','10'), 
    ('11','11'),
    ('12','12'),
    ('13','13'),
    ('14','14'), 
]


class CourtInfoForm(forms.Form):
    name = forms.CharField(max_length=100)
    
    # Location Info
    street_address = forms.CharField(max_length=150)
    city = forms.ModelChoiceField(queryset=City.objects.all())
    geo_position = GeopositionField()
    
    # Court Info
    is_public = forms.BooleanField()
    number_of_courts = forms.ChoiceField(choices=NUMBER_OF_COURT_CHOICES)
    has_lights = forms.BooleanField()
    has_public_washroom = forms.BooleanField()
    surface_type = forms.ChoiceField(choices=SURFACE_TYPE_CHOICES)
    court_info = forms.CharField(widget=forms.Textarea)
    court_condition = forms.CharField(widget=forms.Textarea)
    
