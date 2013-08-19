# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Court.surface_type'
        db.add_column(u'CourtInfo_court', 'surface_type',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Court.surface_type'
        db.delete_column(u'CourtInfo_court', 'surface_type')


    models = {
        u'CourtInfo.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CourtInfo.Province']"})
        },
        u'CourtInfo.country': {
            'Meta': {'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'CourtInfo.court': {
            'Meta': {'object_name': 'Court'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CourtInfo.City']"}),
            'court_condition': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'court_info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fallback_image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'geo_position': ('geoposition.fields.GeopositionField', [], {'max_length': '42'}),
            'has_lights': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number_of_courts': ('django.db.models.fields.IntegerField', [], {'default': '2', 'blank': 'True'}),
            'photosynth_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'surface_type': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'CourtInfo.province': {
            'Meta': {'object_name': 'Province'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CourtInfo.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        u'CourtInfo.thingsnearby': {
            'Meta': {'object_name': 'ThingsNearby'},
            'court': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CourtInfo.Court']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['CourtInfo']