# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'TemplateOS.file_path'
        db.alter_column(u'cicip_templateos', 'file_path', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'TemplateOS.file_path'
        db.alter_column(u'cicip_templateos', 'file_path', self.gf('django.db.models.fields.FilePathField')(max_length=100))

    models = {
        u'cicip.distro': {
            'Meta': {'object_name': 'Distro'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keterangan': ('django.db.models.fields.TextField', [], {}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'cicip.templateos': {
            'Meta': {'object_name': 'TemplateOS'},
            'file_path': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'min_memory': ('django.db.models.fields.IntegerField', [], {})
        },
        u'cicip.version': {
            'Meta': {'object_name': 'Version'},
            'distro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cicip.Distro']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'templateos': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cicip.TemplateOS']"}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cicip']