# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'CourtInfo_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'CourtInfo', ['Country'])

        # Adding model 'Province'
        db.create_table(u'CourtInfo_province', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CourtInfo.Country'])),
        ))
        db.send_create_signal(u'CourtInfo', ['Province'])

        # Adding model 'City'
        db.create_table(u'CourtInfo_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('province', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CourtInfo.Province'])),
        ))
        db.send_create_signal(u'CourtInfo', ['City'])

        # Adding model 'Court'
        db.create_table(u'CourtInfo_court', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('street_address', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CourtInfo.City'])),
            ('geo_position', self.gf('geoposition.fields.GeopositionField')(max_length=42)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('photosynth_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('fallback_image_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('number_of_courts', self.gf('django.db.models.fields.IntegerField')(default=2, blank=True)),
            ('has_lights', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('surface_type', self.gf('django.db.models.fields.IntegerField')(default=4)),
            ('court_info', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('court_condition', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'CourtInfo', ['Court'])

        # Adding model 'ThingsNearby'
        db.create_table(u'CourtInfo_thingsnearby', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('court', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['CourtInfo.Court'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'CourtInfo', ['ThingsNearby'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'CourtInfo_country')

        # Deleting model 'Province'
        db.delete_table(u'CourtInfo_province')

        # Deleting model 'City'
        db.delete_table(u'CourtInfo_city')

        # Deleting model 'Court'
        db.delete_table(u'CourtInfo_court')

        # Deleting model 'ThingsNearby'
        db.delete_table(u'CourtInfo_thingsnearby')


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
            'surface_type': ('django.db.models.fields.IntegerField', [], {'default': '4'})
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