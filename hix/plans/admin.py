from django.contrib import admin
from plans.models import Exchange, Plans


class ExchangeAdmin(admin.ModelAdmin):
  fieldsets = [
  		('Exchange', {'fields': ['exchangename']}),
  		('Address Information',  {'fields': ['exchangeaddress1', 'exchangeadress2', 'exchangecity', 'exchangestate', 'exchangezip'], 'classes': ['collapse']}),
  		('Phone Information',  {'fields': ['exchangephone'], 'classes': ['collapse']}),
  		('Web Information',  {'fields': ['exchangewebsite', 'exchangepublicemail', 'exchangeadminemail'], 'classes': ['collapse']}),
  		('Other Information',  {'fields': ['exchangelegalauirization', 'exchangevisionstatement', 'exchangemaxemployees', 'exchangeinsurancecommission'], 'classes': ['collapse']}),
  		]
		
class PlansAdmin(admin.ModelAdmin):
		list_display = ('planname', 'approved', 'planprice')
  
admin.site.register(Exchange, ExchangeAdmin)
admin.site.register(Plans, PlansAdmin)