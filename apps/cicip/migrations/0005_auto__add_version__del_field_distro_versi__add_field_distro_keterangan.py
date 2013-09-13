# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Version'
        db.create_table(u'cicip_version', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('distro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cicip.Distro'])),
        ))
        db.send_create_signal(u'cicip', ['Version'])

        # Deleting field 'Distro.versi'
        db.delete_column(u'cicip_distro', 'versi')

        # Adding field 'Distro.keterangan'
        db.add_column(u'cicip_distro', 'keterangan',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Version'
        db.delete_table(u'cicip_version')


        # User chose to not deal with backwards NULL issues for 'Distro.versi'
        raise RuntimeError("Cannot reverse this migration. 'Distro.versi' and its values cannot be restored.")
        # Deleting field 'Distro.keterangan'
        db.delete_column(u'cicip_distro', 'keterangan')


    models = {
        u'cicip.distro': {
            'Meta': {'object_name': 'Distro'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keterangan': ('django.db.models.fields.TextField', [], {}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nama': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'cicip.version': {
            'Meta': {'object_name': 'Version'},
            'distro': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cicip.Distro']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cicip']