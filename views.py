from models import *
from annoying.decorators import render_to
from annoying.functions import get_object_or_None
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from datetime import datetime, date, timedelta
from sets import Set
# Create your views here.

def user_login(request):
  if request.method == "POST":
    post = request.POST
    username = post.get("username")
    password = post.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
      if user.is_active:
        login(request,user)
        return HttpResponseRedirect("../expenses/")
    else:
      return HttpResponse("Bad Login")
  elif request.method == "GET":
    return render_to_response("login.html")

class EntrySet(object):
  def __init__(self, heading, values):
    self.heading = heading
    self.values = values

@login_required
@render_to("home.html")
def home(request,
         year=datetime.utcnow().year,
         month=datetime.utcnow().month
         ):
  year,month = int(year),int(month)
  first_of_month = date(year,month,1)
  last_of_month = date(year + (month//12),(month%12)+1,1)-timedelta(1)
  user = request.user
  profile = user.get_profile()
  group = profile.group.all()[0]
  if request.method == "POST":
    post = request.POST
    for category in Category.objects.all():
      vals = post.get(category.name,False)
      if not vals: continue
      numbers = vals.split(" ")
      for number in numbers:
        expense = Expense(
          partner = profile,
          category = category,
          amount = number,
          month_incurred = month,
          year_incurred = year,
        )
        expense.save()

  memberships = Membership.objects.filter(
    group = group,
    begin_date__lte = last_of_month,
    end_date__gte = first_of_month,
    )
  partners = Set([membership.partner for membership in memberships])
  categories = group.category_set.all()
  entry_sets = []
  partner_totals = {}
  for partner in partners:
    partner_totals.setdefault(partner.user.username,0)
  for category in categories:
    values = []
    for partner in partners:
      intersection = Expense.objects.filter(
        partner = partner,
        category = category,
        date_incurred__gte = first_of_month,
        date_incurred__lte = last_of_month,
      )
      total = 0
      for expense in intersection:
        total += expense.amount
      values.append(total)
      partner_totals[partner.user.username] += total
    values.append(sum(values))
    heading = category.name
    entry_set = EntrySet(heading,values)
    entry_sets.append(entry_set)
  ordered_partner_totals = [partner_totals[partner.user.username] for partner in partners]
  total_total = sum(ordered_partner_totals)
  entry_sets.append(EntrySet("Gross Contribution",ordered_partner_totals + [total_total]))
  ordered_diffs = [contributed - (total_total / len(partners)) for contributed in ordered_partner_totals]
  entry_sets.append(EntrySet("Net Contribution",ordered_diffs))
  return {
    'year':year,
    'month':month,
    'headers':[r.user.first_name+" "+r.user.last_name for r in partners]+["Totals"],
    'entry_sets':entry_sets,
    'categories':categories,
    }

def logout_user(request):
  logout(request)
  return HttpResponseRedirect("login")

class CategoryExpenseCombo(object):
  def __init__(self, category, target):
    self.category = category
    self.target = target

@login_required
@render_to("spending_targets.html")
def spending_target(request):
  if request.method == "POST":
    post = request.POST
    for category in Category.objects.all():
      value = post.get(category.name,False)
      if not value: continue
      target = get_object_or_None(Target, category = category)
      if not target:
        target = Target(category = category)
      target.amount = value
      target.save()

  category_targets = []
  for category in Category.objects.all():
    target = get_object_or_None(Target, category = category)
    category_target = CategoryExpenseCombo(category, target)
    category_targets.append(category_target)

  return {
  	"category_targets":	category_targets,
	}
