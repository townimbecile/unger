from django.db import models
from django.contrib.auth.models import User
from django import forms
import datetime

MONTHS = (
  ( 1 , "January"   ),
  ( 2 , "February"  ),
  ( 3 , "March"     ),
  ( 4 , "April"     ),
  ( 5 , "May"       ),
  ( 6 , "June"      ),
  ( 7 , "July"      ),
  ( 8 , "August"    ),
  ( 9 , "September" ),
  ( 10, "October"   ),
  ( 11, "November"  ),
  ( 12, "December"  ),
)

# Create your models here.

class ExpenseSet(object):
  def getMonthlyTotal(self, int_month, int_year):
    relevant_expenses = self.expense_set.filter(
      month_incurred = int_month,
      year_incurred = int_year,
    )
    tally = 0
    for expense in relevant_expenses:
      tally += expense.amount
    return tally

class Group(models.Model,ExpenseSet):
  name = models.CharField(max_length=255)

  def __unicode__(self):
    return self.name

class Category(models.Model,ExpenseSet):
  name = models.CharField(max_length=255)
  group = models.ForeignKey(Group)

  def __unicode__(self):
    return self.name
  
  class Meta:
    verbose_name_plural = "Categories"

class Target(models.Model):
  category = models.ForeignKey(Category, unique = True)
  amount = models.DecimalField(max_digits=5, decimal_places=2)

class Partner(models.Model,ExpenseSet):
  user = models.ForeignKey(User, unique=True)
  group = models.ManyToManyField(Group, through='Membership')

  def __unicode__(self):
    return self.user.username

class Membership(models.Model):
  partner = models.ForeignKey(Partner)
  group = models.ForeignKey(Group)
  begin_date = models.DateField(blank=True,null=True)
  end_date = models.DateField(blank=True,null=True)

  def clean_dates(self):
    if not self.begin_date:
      self.begin_date = datetime.date.min
    if not self.end_date:
      self.end_date = datetime.date.max
    
  def save(self, *args, **kwargs):
    self.clean_dates()
    if self.begin_date > self.end_date:
      raise forms.ValidationError("begin_date must be earlier than end date")
    else:
      return super(Membership,self).save()

class Expense(models.Model):
  partner = models.ForeignKey(Partner)
  category = models.ForeignKey(Category)
  amount = models.DecimalField(max_digits=5, decimal_places=2)
  date_created = models.DateField(auto_now_add=True)
  date_incurred = models.DateField(auto_now_add=True)

  def __unicode__(self):
    return "%s -- %s : %s (%s, %s)"%(
      self.partner,
      self.category,
      self.amount,
      self.get_month_incurred_display(),
      self.year_incurred,
      )

