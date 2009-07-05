
from south.db import db
from django.db import models
from dberger_web.unger.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Expense.date_created'
        db.add_column('unger_expense', 'date_created', models.DateTimeField(auto_now_add=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Expense.date_created'
        db.delete_column('unger_expense', 'date_created')
        
    
    
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
            'begin_date': ('models.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('models.DateField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('models.ForeignKey', ['Group'], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'partner': ('models.ForeignKey', ['Partner'], {})
        },
        'unger.category': {
            'group': ('models.ForeignKey', ['Group'], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '255'})
        },
        'unger.expense': {
            'amount': ('models.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'category': ('models.ForeignKey', ['Category'], {}),
            'date_created': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'date_incurred': ('models.DateField', [], {'auto_now_add': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'partner': ('models.ForeignKey', ['Partner'], {})
        }
    }
    
    complete_apps = ['unger']
