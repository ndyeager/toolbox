from django.contrib import admin
from .models import *

class RosterInLine(admin.StackedInline):
	model = ClassRoster
	extra = 1

class ClassAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 					{'fields': ['className']}),
		('Class Information',	{'fields': ['teacher', 'classId'], 'classes':['collapse']}),
	]
	inlines = [RosterInLine]
	list_display = ('className', 'classId', 'teacher')
	list_filter = ['className']
	search_fields = ['classId']

admin.site.register(Class, ClassAdmin)