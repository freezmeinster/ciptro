# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Distro'
        db.create_table(u'cicip_distro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nama', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('versi', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'cicip', ['Distro'])


    def backwards(self, orm):
        # Deleting model 'Distro'
        db.delete_table(u'cicip_distro')


    models = {
        u'cicip.distro': {
            'Meta': {'object_name': 'Distro'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'versi': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'cicip.pengguna': {
            'Meta': {'object_name': 'Pengguna'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cicip']