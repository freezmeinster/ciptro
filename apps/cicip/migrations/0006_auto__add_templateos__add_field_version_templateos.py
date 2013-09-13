# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TemplateOS'
        db.create_table(u'cicip_templateos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file_path', self.gf('django.db.models.fields.FilePathField')(max_length=100)),
            ('min_memory', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'cicip', ['TemplateOS'])

        # Adding field 'Version.templateos'
        db.add_column(u'cicip_version', 'templateos',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['cicip.TemplateOS']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'TemplateOS'
        db.delete_table(u'cicip_templateos')

        # Deleting field 'Version.templateos'
        db.delete_column(u'cicip_version', 'templateos_id')


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
            'file_path': ('django.db.models.fields.FilePathField', [], {'max_length': '100'}),
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