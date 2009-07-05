
from south.db import db
from django.db import models
from dberger_web.unger.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Group'
        db.create_table('unger_group', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=255)),
        ))
        db.send_create_signal('unger', ['Group'])
        
        # Adding model 'Target'
        db.create_table('unger_target', (
            ('category', models.ForeignKey(orm.Category, unique=True)),
            ('amount', models.DecimalField(max_digits=5, decimal_places=2)),
            ('id', models.AutoField(primary_key=True)),
        ))
        db.send_create_signal('unger', ['Target'])
        
        # Adding model 'Partner'
        db.create_table('unger_partner', (
            ('id', models.AutoField(primary_key=True)),
            ('user', models.ForeignKey(orm['auth.User'], unique=True)),
        ))
        db.send_create_signal('unger', ['Partner'])
        
        # Adding model 'Membership'
        db.create_table('unger_membership', (
            ('partner', models.ForeignKey(orm.Partner)),
            ('group', models.ForeignKey(orm.Group)),
            ('id', models.AutoField(primary_key=True)),
        ))
        db.send_create_signal('unger', ['Membership'])
        
        # Adding model 'DateRange'
        db.create_table('unger_daterange', (
            ('begin_date', models.DateField()),
            ('id', models.AutoField(primary_key=True)),
            ('end_date', models.DateField()),
        ))
        db.send_create_signal('unger', ['DateRange'])
        
        # Adding model 'Expense'
        db.create_table('unger_expense', (
            ('category', models.ForeignKey(orm.Category)),
            ('year_incurred', models.IntegerField()),
            ('amount', models.DecimalField(max_digits=5, decimal_places=2)),
            ('month_incurred', models.IntegerField()),
            ('date_created', models.DateTimeField(auto_now_add=True)),
            ('partner', models.ForeignKey(orm.Partner)),
            ('id', models.AutoField(primary_key=True)),
        ))
        db.send_create_signal('unger', ['Expense'])
        
        # Adding model 'Category'
        db.create_table('unger_category', (
            ('id', models.AutoField(primary_key=True)),
            ('name', models.CharField(max_length=255)),
        ))
        db.send_create_signal('unger', ['Category'])
        
        # Adding ManyToManyField 'Membership.participation_interval'
        db.create_table('unger_membership_participation_interval', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membership', models.ForeignKey(Membership, null=False)),
            ('daterange', models.ForeignKey(DateRange, null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Group'
        db.delete_table('unger_group')
        
        # Deleting model 'Target'
        db.delete_table('unger_target')
        
        # Deleting model 'Partner'
        db.delete_table('unger_partner')
        
        # Deleting model 'Membership'
        db.delete_table('unger_membership')
        
        # Deleting model 'DateRange'
        db.delete_table('unger_daterange')
        
        # Deleting model 'Expense'
        db.delete_table('unger_expense')
        
        # Deleting model 'Category'
        db.delete_table('unger_category')
        
        # Dropping ManyToManyField 'Membership.participation_interval'
        db.delete_table('unger_membership_participation_interval')
        
    
    
    models = {
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'unger.group': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '255'})
        },
        'unger.target': {
            'amount': ('models.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'category': ('models.ForeignKey', ['Category'], {'unique': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'unger.partner': {
            'group': ('models.ManyToManyField', ['Group'], {'through': "'Membership'"}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'user': ('models.ForeignKey', ['User'], {'unique': 'True'})
        },
        'unger.membership': {
            'group': ('models.ForeignKey', ['Group'], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'participation_interval': ('models.ManyToManyField', ['DateRange'], {}),
            'partner': ('models.ForeignKey', ['Partner'], {})
        },
        'unger.daterange': {
            'begin_date': ('models.DateField', [], {}),
            'end_date': ('models.DateField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'unger.expense': {
            'amount': ('models.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'category': ('models.ForeignKey', ['Category'], {}),
            'date_created': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'month_incurred': ('models.IntegerField', [], {}),
            'partner': ('models.ForeignKey', ['Partner'], {}),
            'year_incurred': ('models.IntegerField', [], {})
        },
        'unger.category': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '255'})
        }
    }
    
    complete_apps = ['unger']
