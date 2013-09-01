from django.contrib import admin
from CourtInfo.models import Country, Province, City, Court, ThingsNearby, CourtPhoto


class ThingsNearbyInline(admin.TabularInline):
    model = ThingsNearby
    extra = 3
    
class CourtPhotoInline(admin.TabularInline):
    model = CourtPhoto
    extra = 0

class CourtAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,   { 'fields': ['name', 'slug']}),
        ('Location', { 'fields': ['street_address', 'city', 'geo_position']}),
        ('Visuals', {'fields': ['photosynth_url']}),
        ('Details', {'fields': ['is_public', 'number_of_courts', 'has_lights', 'has_public_washroom', 'surface_type', 'court_info', 'court_condition']}),
    ]
    inlines = [ThingsNearbyInline, CourtPhotoInline]
    
    # The fields that display in the admin court list
    list_display = ('name', 'city')

    
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(Court, CourtAdmin)
