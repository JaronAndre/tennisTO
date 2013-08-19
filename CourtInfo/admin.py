from django.contrib import admin
from CourtInfo.models import Country, Province, City, Court, ThingsNearby


class ThingsNearbyInline(admin.TabularInline):
    model = ThingsNearby
    extra = 3

class CourtAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,   { 'fields': ['name', 'slug']}),
        ('Location', { 'fields': ['street_address', 'city', 'geo_position']}),
        ('Visuals', {'fields': ['photosynth_url']}),
        ('Details', {'fields': ['is_public', 'number_of_courts', 'has_lights', 'surface_type', 'court_info', 'court_condition']}),
    ]
    inlines = [ThingsNearbyInline]
    
    # The fields that display in the admin court list
    list_display = ('name', 'city')

    
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(Court, CourtAdmin)
