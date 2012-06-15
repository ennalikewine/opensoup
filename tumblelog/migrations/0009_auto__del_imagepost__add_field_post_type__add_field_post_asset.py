# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ImagePost'
        db.delete_table('tumblelog_imagepost')

        # Adding field 'Post.type'
        db.add_column('tumblelog_post', 'type',
                      self.gf('django.db.models.fields.CharField')(default='IM', max_length=2),
                      keep_default=False)

        # Adding field 'Post.asset'
        db.add_column('tumblelog_post', 'asset',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tumblelog.Asset'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'ImagePost'
        db.create_table('tumblelog_imagepost', (
            ('post_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tumblelog.Post'], unique=True, primary_key=True)),
            ('asset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tumblelog.Asset'])),
        ))
        db.send_create_signal('tumblelog', ['ImagePost'])

        # Deleting field 'Post.type'
        db.delete_column('tumblelog_post', 'type')

        # Deleting field 'Post.asset'
        db.delete_column('tumblelog_post', 'asset_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'tumblelog.asset': {
            'Meta': {'object_name': 'Asset'},
            'directory': ('django.db.models.fields.IntegerField', [], {}),
            'diskfile': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'random_part': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'})
        },
        'tumblelog.blog': {
            'Meta': {'object_name': 'Blog'},
            'avatar': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tumblelog.Asset']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'tumblelog.post': {
            'Meta': {'object_name': 'Post'},
            'asset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tumblelog.Asset']", 'null': 'True', 'blank': 'True'}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tumblelog.Blog']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'post_origin'", 'null': 'True', 'to': "orm['tumblelog.Post']"}),
            'reposted_via': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'post_reposted_via'", 'null': 'True', 'to': "orm['tumblelog.Post']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'})
        },
        'tumblelog.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'following': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'following'", 'blank': 'True', 'to': "orm['tumblelog.Blog']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['tumblelog']