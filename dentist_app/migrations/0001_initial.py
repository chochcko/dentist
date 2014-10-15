# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HomePage'
        db.create_table('dentist_app_homepage', (
            ('page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, unique=True, to=orm['pages.Page'])),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('heading', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('subheading', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('featured_works_heading', self.gf('django.db.models.fields.CharField')(max_length=200, default='Featured Works')),
            ('featured_portfolio', self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, to=orm['dentist_app.Portfolio'])),
            ('content_heading', self.gf('django.db.models.fields.CharField')(max_length=200, default='About us!')),
            ('latest_posts_heading', self.gf('django.db.models.fields.CharField')(max_length=200, default='Latest Posts')),
        ))
        db.send_create_signal('dentist_app', ['HomePage'])

        # Adding model 'Slide'
        db.create_table('dentist_app_slide', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_order', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('homepage', self.gf('django.db.models.fields.related.ForeignKey')(related_name='slides', to=orm['dentist_app.HomePage'])),
            ('image', self.gf('mezzanine.core.fields.FileField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('dentist_app', ['Slide'])

        # Adding model 'Portfolio'
        db.create_table('dentist_app_portfolio', (
            ('page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, unique=True, to=orm['pages.Page'])),
        ))
        db.send_create_signal('dentist_app', ['Portfolio'])


    def backwards(self, orm):
        # Deleting model 'HomePage'
        db.delete_table('dentist_app_homepage')

        # Deleting model 'Slide'
        db.delete_table('dentist_app_slide')

        # Deleting model 'Portfolio'
        db.delete_table('dentist_app_portfolio')


    models = {
        'dentist_app.homepage': {
            'Meta': {'_ormbases': ['pages.Page'], 'ordering': "('_order',)", 'object_name': 'HomePage'},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'content_heading': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "'About us!'"}),
            'featured_portfolio': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['dentist_app.Portfolio']"}),
            'featured_works_heading': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "'Featured Works'"}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'latest_posts_heading': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "'Latest Posts'"}),
            'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'unique': 'True', 'to': "orm['pages.Page']"}),
            'subheading': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'dentist_app.portfolio': {
            'Meta': {'_ormbases': ['pages.Page'], 'ordering': "('_order',)", 'object_name': 'Portfolio'},
            'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'unique': 'True', 'to': "orm['pages.Page']"})
        },
        'dentist_app.slide': {
            'Meta': {'object_name': 'Slide', 'ordering': "('_order',)"},
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'homepage': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'slides'", 'to': "orm['dentist_app.HomePage']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('mezzanine.core.fields.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'pages.page': {
            'Meta': {'object_name': 'Page', 'ordering': "('titles',)"},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'max_length': '100', 'null': 'True', 'blank': 'True', 'default': '(1, 2, 3)'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'null': 'True', 'blank': 'True', 'to': "orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        'sites.site': {
            'Meta': {'object_name': 'Site', 'ordering': "('domain',)", 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['dentist_app']