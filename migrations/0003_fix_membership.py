
from south.db import db
from django.db import models
from dberger_web.unger.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Membership.end_date'
        db.add_column('unger_membership', 'end_date', models.DateField())
        
        # Adding field 'Membership.begin_date'
        db.add_column('unger_membership', 'begin_date', models.DateField())
        
        # Dropping ManyToManyField 'Membership.participation_interval'
        db.delete_table('unger_membership_participation_interval')
        
        # Deleting model 'daterange'
        db.delete_table('unger_daterange')
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Membership.end_date'
        db.delete_column('unger_membership', 'end_date')
        
        # Deleting field 'Membership.begin_date'
        db.delete_column('unger_membership', 'begin_date')
        
        # Adding ManyToManyField 'Membership.participation_interval'
        db.create_table('unger_membership_participation_interval', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membership', models.ForeignKey(Membership, null=False)),
            ('daterange', models.ForeignKey(daterange, null=False))
        ))
        
        # Adding model 'daterange'
        db.create_table('unger_daterange', (
            ('begin_date', models.DateField()),
            ('id', models.AutoField(primary_key=True)),
            ('end_date', models.DateField()),
        ))
        db.send_create_signal('unger', ['daterange'])
        
    
    
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
            'begin_date': ('models.DateField', [], {}),
            'end_date': ('models.DateField', [], {}),
            'group': ('models.ForeignKey', ['Group'], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'partner': ('models.ForeignKey', ['Partner'], {})
        },
        'unger.category': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '255'})
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
        'unger.daterange': {
            '_stub': True,
            'id': 'models.AutoField(primary_key=True)'
        }
    }
    
    complete_apps = ['unger']
