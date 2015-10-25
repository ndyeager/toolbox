from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Admin)
admin.site.register(Student)