# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subscriber'
        db.create_table(u'core_subscriber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
        ))
        db.send_create_signal(u'core', ['Subscriber'])

        # Adding model 'Spot'
        db.create_table(u'core_spot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')(default='San Francisco', unique=True)),
            ('url', self.gf('django.db.models.fields.TextField')(default='http://ndbc.noaa.gov/data/5day2/42012_5day.txt', unique=True)),
        ))
        db.send_create_signal(u'core', ['Spot'])

        # Adding model 'ForecastData'
        db.create_table(u'core_forecastdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('WDIR', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('WSPD', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('GST', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('WVHT', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('DPD', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('APD', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('MWD', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('PRES', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('ATMP', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('WTMP', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('DEWP', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('VIS', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('PTDY', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('TIDE', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('spot', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['core.Spot'])),
        ))
        db.send_create_signal(u'core', ['ForecastData'])

        # Adding unique constraint on 'ForecastData', fields ['spot', 'date']
        db.create_unique(u'core_forecastdata', ['spot_id', 'date'])

        # Adding model 'ImageData'
        db.create_table(u'core_imagedata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['core.ForecastData'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['ImageData'])


    def backwards(self, orm):
        # Removing unique constraint on 'ForecastData', fields ['spot', 'date']
        db.delete_unique(u'core_forecastdata', ['spot_id', 'date'])

        # Deleting model 'Subscriber'
        db.delete_table(u'core_subscriber')

        # Deleting model 'Spot'
        db.delete_table(u'core_spot')

        # Deleting model 'ForecastData'
        db.delete_table(u'core_forecastdata')

        # Deleting model 'ImageData'
        db.delete_table(u'core_imagedata')


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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'core.spot': {
            'Meta': {'object_name': 'Spot'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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