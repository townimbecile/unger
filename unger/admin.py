from dberger_web.unger import models
from django.contrib import admin
from django.forms import ModelForm

admin.site.register(models.Category)
admin.site.register(models.Expense)
class MembershipInline(admin.TabularInline):
  model = models.Membership
  extra = 1
class PartnerAdmin(admin.ModelAdmin):
  inlines = (MembershipInline,)
class GroupAdmin(admin.ModelAdmin):
  inlines = (MembershipInline,)
admin.site.register(models.Partner, PartnerAdmin)
admin.site.register(models.Group, GroupAdmin)
