# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImageLink'
        db.create_table(u'core_imagelink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.TextField')()),
            ('ForecastData', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['core.ForecastData'], null=True)),
        ))
        db.send_create_signal(u'core', ['ImageLink'])


    def backwards(self, orm):
        # Deleting model 'ImageLink'
        db.delete_table(u'core_imagelink')


    models = {
        u'core.forecastdata': {
            'APD': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'ATMP': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'DEWP': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'DPD': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'GST': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'MWD': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Meta': {'unique_together': "(('spot', 'date'),)", 'object_name': 'ForecastData'},
            'PRES': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'PTDY': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'TIDE': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'VIS': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'WDIR': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'WSPD': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'WTMP': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'WVHT': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spot': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['core.Spot']"})
        },
        u'core.imagedata': {
            'Meta': {'object_name': 'ImageData'},
            'data': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['core.ForecastData']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'spot': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['core.Spot']"})
        },
        u'core.imagelink': {
            'ForecastData': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['core.ForecastData']", 'null': 'True'}),
            'Meta': {'object_name': 'ImageLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {})
        },
        u'core.spot': {
            'Meta': {'object_name': 'Spot'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'default': "'San Francisco'", 'unique': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'default': "'http://ndbc.noaa.gov/data/5day2/42012_5day.txt'", 'unique': 'True'})
        },
        u'core.subscriber': {
            'Meta': {'object_name': 'Subscriber'},
            'email_address': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['core']