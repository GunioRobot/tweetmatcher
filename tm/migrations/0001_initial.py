# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Author'
        db.create_table('tm_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('twitter_username', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('tm', ['Author'])

        # Adding model 'Tag'
        db.create_table('tm_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('tm', ['Tag'])

        # Adding M2M table for field authors on 'Tag'
        db.create_table('tm_tag_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm['tm.tag'], null=False)),
            ('author', models.ForeignKey(orm['tm.author'], null=False))
        ))
        db.create_unique('tm_tag_authors', ['tag_id', 'author_id'])

        # Adding model 'Tweet'
        db.create_table('tm_tweet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tm.Author'])),
        ))
        db.send_create_signal('tm', ['Tweet'])

        # Adding model 'Hashtag'
        db.create_table('tm_hashtag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=139)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tm.Author'])),
        ))
        db.send_create_signal('tm', ['Hashtag'])

        # Adding model 'Mention'
        db.create_table('tm_mention', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=139)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tm.Author'])),
        ))
        db.send_create_signal('tm', ['Mention'])


    def backwards(self, orm):
        
        # Deleting model 'Author'
        db.delete_table('tm_author')

        # Deleting model 'Tag'
        db.delete_table('tm_tag')

        # Removing M2M table for field authors on 'Tag'
        db.delete_table('tm_tag_authors')

        # Deleting model 'Tweet'
        db.delete_table('tm_tweet')

        # Deleting model 'Hashtag'
        db.delete_table('tm_hashtag')

        # Deleting model 'Mention'
        db.delete_table('tm_mention')


    models = {
        'tm.author': {
            'Meta': {'object_name': 'Author'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'twitter_username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'tm.hashtag': {
            'Meta': {'object_name': 'Hashtag'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tm.Author']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '139'})
        },
        'tm.mention': {
            'Meta': {'object_name': 'Mention'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tm.Author']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '139'})
        },
        'tm.tag': {
            'Meta': {'object_name': 'Tag'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tm.Author']", 'symmetrical': 'False'}),
            'body': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tm.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tm.Author']"}),
            'body': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['tm']
