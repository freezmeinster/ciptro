# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Distro.logo'
        db.add_column(u'cicip_distro', 'logo',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Distro.logo'
        db.delete_column(u'cicip_distro', 'logo')


    models = {
        u'cicip.distro': {
            'Meta': {'object_name': 'Distro'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'versi': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cicip']