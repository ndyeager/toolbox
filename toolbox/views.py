from django.shortcuts import render

from users.models import *
from classes.models import *

def home(request):
	user = Teacher.objects.get(pk=User.objects.filter(user_type="Teacher").get(firstName="Amanda").id)

	print user.classes.all()

	classes = user.classes.all()

	context = {
		'user' : user,
		'classes' : classes
	}


	return render(request, 'home.html', context)