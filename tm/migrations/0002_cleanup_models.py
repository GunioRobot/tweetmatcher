# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Tag'
        db.delete_table('tm_tag')

        # Removing M2M table for field authors on 'Tag'
        db.delete_table('tm_tag_authors')

        # Deleting field 'Author.twitter_username'
        db.delete_column('tm_author', 'twitter_username')

        # Deleting field 'Author.email'
        db.delete_column('tm_author', 'email')

        # Adding field 'Author.username'
        db.add_column('tm_author', 'username', self.gf('django.db.models.fields.CharField')(default='bogus', unique=True, max_length=30), keep_default=False)

        # Adding field 'Author.screen_name'
        db.add_column('tm_author', 'screen_name', self.gf('django.db.models.fields.CharField')(default='bogus', max_length=100), keep_default=False)

        # Adding field 'Author.profile_image_url'
        db.add_column('tm_author', 'profile_image_url', self.gf('django.db.models.fields.URLField')(default='bogus', max_length=200), keep_default=False)

        # Adding field 'Tweet.twitter_id'
        db.add_column('tm_tweet', 'twitter_id', self.gf('django.db.models.fields.BigIntegerField')(default=0, unique=True), keep_default=False)

        # Adding field 'Tweet.created_at'
        db.add_column('tm_tweet', 'created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 4, 2, 16, 8, 16, 826487)), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'Tag'
        db.create_table('tm_tag', (
            ('body', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('tm', ['Tag'])

        # Adding M2M table for field authors on 'Tag'
        db.create_table('tm_tag_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm['tm.tag'], null=False)),
            ('author', models.ForeignKey(orm['tm.author'], null=False))
        ))
        db.create_unique('tm_tag_authors', ['tag_id', 'author_id'])

        # User chose to not deal with backwards NULL issues for 'Author.twitter_username'
        raise RuntimeError("Cannot reverse this migration. 'Author.twitter_username' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Author.email'
        raise RuntimeError("Cannot reverse this migration. 'Author.email' and its values cannot be restored.")

        # Deleting field 'Author.username'
        db.delete_column('tm_author', 'username')

        # Deleting field 'Author.screen_name'
        db.delete_column('tm_author', 'screen_name')

        # Deleting field 'Author.profile_image_url'
        db.delete_column('tm_author', 'profile_image_url')

        # Deleting field 'Tweet.twitter_id'
        db.delete_column('tm_tweet', 'twitter_id')

        # Deleting field 'Tweet.created_at'
        db.delete_column('tm_tweet', 'created_at')


    models = {
        'tm.author': {
            'Meta': {'object_name': 'Author'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile_image_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'screen_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
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
        'tm.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tm.Author']"}),
            'body': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'twitter_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'})
        }
    }

    complete_apps = ['tm']
