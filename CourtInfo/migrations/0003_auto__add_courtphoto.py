# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CourtPhoto'
        db.create_table(u'CourtInfo_courtphoto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('court', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CourtInfo.Court'])),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('time_added', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('is_validated', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'CourtInfo', ['CourtPhoto'])


    def backwards(self, orm):
        # Deleting model 'CourtPhoto'
        db.delete_table(u'CourtInfo_courtphoto')


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
            'has_public_washroom': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number_of_courts': ('django.db.models.fields.IntegerField', [], {'default': '2', 'blank': 'True'}),
            'photosynth_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'surface_type': ('django.db.models.fields.IntegerField', [], {'default': '4'})
        },
        u'CourtInfo.courtphoto': {
            'Meta': {'object_name': 'CourtPhoto'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'court': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['CourtInfo.Court']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'is_validated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time_added': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
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