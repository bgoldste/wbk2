# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Spot', fields ['url']
        db.create_unique(u'core_spot', ['url'])

        # Adding unique constraint on 'Spot', fields ['name']
        db.create_unique(u'core_spot', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Spot', fields ['name']
        db.delete_unique(u'core_spot', ['name'])

        # Removing unique constraint on 'Spot', fields ['url']
        db.delete_unique(u'core_spot', ['url'])


    models = {
        u'core.forecastdata': {
            'APD': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'ATMP': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'DEWP': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'DPD': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'GST': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'MWD': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Meta': {'unique_together': "(('date', 'spot'),)", 'object_name': 'ForecastData'},
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
            'spot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Spot']", 'null': 'True'})
        },
        u'core.spot': {
            'Meta': {'object_name': 'Spot'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {'default': "'San Francisco'", 'unique': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {'default': "'http://ndbc.noaa.gov/data/5day2/42012_5day.txt'", 'unique': 'True'})
        },
        u'core.subscriber': {
            'Meta': {'object_name': 'Subscriber'},
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['core']