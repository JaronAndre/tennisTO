from django.contrib import admin
from CourtInfo.models import Court, ThingsNearby

class ThingsNearbyInline(admin.TabularInline):
    model = ThingsNearby
    extra = 3

class CourtAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,   { 'fields': ['name', 'slug', 'geo_position', 'full_address']}), 
        ('Visuals', {'fields': ['photosynth_url']}),
        ('Details', {'fields': ['court_info', 'court_condition']}),
    ]
    inlines = [ThingsNearbyInline]

admin.site.register(Court, CourtAdmin)
