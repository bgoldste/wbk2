# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ForecastData.WDIR'
        db.add_column(u'core_forecastdata', 'WDIR',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'ForecastData.WSPD'
        db.add_column(u'core_forecastdata', 'WSPD',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'ForecastData.GST'
        db.add_column(u'core_forecastdata', 'GST',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'ForecastData.WVHT'
        db.add_column(u'core_forecastdata', 'WVHT',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'ForecastData.DPD'
        db.add_column(u'core_forecastdata', 'DPD',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'ForecastData.APD'
        db.add_column(u'core_forecastdata', 'APD',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'ForecastData.MWD'
        db.add_column(u'core_forecastdata', 'MWD',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'ForecastData.PRES'
        db.add_column(u'core_forecastdata', 'PRES',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'ForecastData.ATMP'
        db.add_column(u'core_forecastdata', 'ATMP',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'ForecastData.WTMP'
        db.add_column(u'core_forecastdata', 'WTMP',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'ForecastData.DEWP'
        db.add_column(u'core_forecastdata', 'DEWP',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'ForecastData.VIS'
        db.add_column(u'core_forecastdata', 'VIS',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'ForecastData.PTDY'
        db.add_column(u'core_forecastdata', 'PTDY',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'ForecastData.TIDE'
        db.add_column(u'core_forecastdata', 'TIDE',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ForecastData.WDIR'
        db.delete_column(u'core_forecastdata', 'WDIR')

        # Deleting field 'ForecastData.WSPD'
        db.delete_column(u'core_forecastdata', 'WSPD')

        # Deleting field 'ForecastData.GST'
        db.delete_column(u'core_forecastdata', 'GST')

        # Deleting field 'ForecastData.WVHT'
        db.delete_column(u'core_forecastdata', 'WVHT')

        # Deleting field 'ForecastData.DPD'
        db.delete_column(u'core_forecastdata', 'DPD')

        # Deleting field 'ForecastData.APD'
        db.delete_column(u'core_forecastdata', 'APD')

        # Deleting field 'ForecastData.MWD'
        db.delete_column(u'core_forecastdata', 'MWD')

        # Deleting field 'ForecastData.PRES'
        db.delete_column(u'core_forecastdata', 'PRES')

        # Deleting field 'ForecastData.ATMP'
        db.delete_column(u'core_forecastdata', 'ATMP')

        # Deleting field 'ForecastData.WTMP'
        db.delete_column(u'core_forecastdata', 'WTMP')

        # Deleting field 'ForecastData.DEWP'
        db.delete_column(u'core_forecastdata', 'DEWP')

        # Deleting field 'ForecastData.VIS'
        db.delete_column(u'core_forecastdata', 'VIS')

        # Deleting field 'ForecastData.PTDY'
        db.delete_column(u'core_forecastdata', 'PTDY')

        # Deleting field 'ForecastData.TIDE'
        db.delete_column(u'core_forecastdata', 'TIDE')


    models = {
        u'core.forecastdata': {
            'APD': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'ATMP': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'DEWP': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'DPD': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'GST': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'MWD': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Meta': {'object_name': 'ForecastData'},
            'PRES': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'PTDY': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'TIDE': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'VIS': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'WDIR': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'WSPD': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'WTMP': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'WVHT': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.subscriber': {
            'Meta': {'object_name': 'Subscriber'},
            'email_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['core']