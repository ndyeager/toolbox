from django.db import models


# Model for users with three user types (Teacher, Student and Administrator)
class User(models.Model):
	firstName = models.CharField(max_length=60)
	lastName = models.CharField(max_length=60)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=255)
	ADMINISTRATOR = "Administrator"
	TEACHER = 'Teacher'
	STUDENT = 'Student'
	USER_TYPE = (
		(ADMINISTRATOR, "Administrator"),
		(TEACHER, 'Teacher'),
		(STUDENT, 'Student'),
	)
	user_type = models.CharField(max_length=20, choices=USER_TYPE, default=TEACHER)

	# Returns user object's first and last name 
	def __unicode__(self):
		return self.firstName + " " + self.lastName

# Model for Teachers
class Teacher(models.Model):
	fullName = models.ForeignKey(User, limit_choices_to={'user_type':"Teacher"})
	teacherId = models.CharField(max_length=20, unique=True)
	schoolId = models.CharField(max_length=20)

	# Returns user object's first and last name 
	def __unicode__(self):
		return str(self.fullName)

# Model for Admins
class Admin(models.Model):
	fullName = models.ForeignKey(User, limit_choices_to={'user_type':"Administrator"})
	schoolId = models.CharField(max_length=20)
	schoolName = models.CharField(max_length=60)
	city = models.CharField(max_length=60)
	state = models.CharField(max_length=2)

	# Returns user object's first and last name 
	def __unicode__(self):
		return str(self.fullName)

# Model for Students
class Student(models.Model):
	fullName = models.ForeignKey(User, limit_choices_to={'user_type':'Student'})
	studentId = models.CharField(max_length=20, unique=True)
	schoolId = models.CharField(max_length=20)
	
	# Returns user object's first and last name 
	def __unicode__(self):
		return str(self.fullName)






