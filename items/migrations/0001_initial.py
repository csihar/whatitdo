# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'items_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item_creator', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('progress', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('finished', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rating', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
        ))
        db.send_create_signal(u'items', ['Item'])

        # Adding model 'UserProfile'
        db.create_table(u'items_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('userpic', self.gf('django.db.models.fields.files.ImageField')(default='userpics/default.png', max_length=100)),
            ('link1', self.gf('django.db.models.fields.URLField')(max_length=100, blank=True)),
            ('link2', self.gf('django.db.models.fields.URLField')(max_length=100, blank=True)),
            ('link3', self.gf('django.db.models.fields.URLField')(max_length=100, blank=True)),
            ('tvsort1', self.gf('django.db.models.fields.CharField')(default='name', max_length=10)),
            ('tvsort2', self.gf('django.db.models.fields.CharField')(default='name', max_length=10)),
            ('moviesort1', self.gf('django.db.models.fields.CharField')(default='name', max_length=10)),
            ('moviesort2', self.gf('django.db.models.fields.CharField')(default='name', max_length=10)),
            ('booksort1', self.gf('django.db.models.fields.CharField')(default='name', max_length=10)),
            ('booksort2', self.gf('django.db.models.fields.CharField')(default='name', max_length=10)),
            ('gamesort1', self.gf('django.db.models.fields.CharField')(default='name', max_length=10)),
            ('gamesort2', self.gf('django.db.models.fields.CharField')(default='name', max_length=10)),
            ('musicsort1', self.gf('django.db.models.fields.CharField')(default='artist', max_length=10)),
            ('musicsort2', self.gf('django.db.models.fields.CharField')(default='name', max_length=10)),
        ))
        db.send_create_signal(u'items', ['UserProfile'])

        # Adding model 'Contact'
        db.create_table(u'items_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'items', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'items_item')

        # Deleting model 'UserProfile'
        db.delete_table(u'items_userprofile')

        # Deleting model 'Contact'
        db.delete_table(u'items_contact')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'items.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'})
        },
        u'items.item': {
            'Meta': {'object_name': 'Item'},
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'finished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_creator': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'progress': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'items.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'booksort1': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '10'}),
            'booksort2': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '10'}),
            'gamesort1': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '10'}),
            'gamesort2': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link1': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'link2': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'link3': ('django.db.models.fields.URLField', [], {'max_length': '100', 'blank': 'True'}),
            'moviesort1': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '10'}),
            'moviesort2': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '10'}),
            'musicsort1': ('django.db.models.fields.CharField', [], {'default': "'artist'", 'max_length': '10'}),
            'musicsort2': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '10'}),
            'tvsort1': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '10'}),
            'tvsort2': ('django.db.models.fields.CharField', [], {'default': "'name'", 'max_length': '10'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'userpic': ('django.db.models.fields.files.ImageField', [], {'default': "'userpics/default.png'", 'max_length': '100'})
        }
    }

    complete_apps = ['items']