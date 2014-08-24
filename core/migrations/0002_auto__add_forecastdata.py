# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ForecastData'
        db.create_table(u'core_forecastdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'core', ['ForecastData'])


    def backwards(self, orm):
        # Deleting model 'ForecastData'
        db.delete_table(u'core_forecastdata')


    models = {
        u'core.forecastdata': {
            'Meta': {'object_name': 'ForecastData'},
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