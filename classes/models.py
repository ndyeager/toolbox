from django.db import models
from users.models import *

class Class(models.Model):
	teacher = models.ForeignKey(Teacher, related_name='classes')
	className = models.CharField(max_length=60)
	classId = models.CharField(max_length=20, unique=True)

	def __unicode__(self):
		return self.className

class ClassRoster(models.Model):
	className = models.ForeignKey(Class)
	student = models.ForeignKey(Student)

	def __unicode__(self):
		return str(self.className)
