from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from btp import choices
import datetime

class Application(models.Model):
	name = models.CharField(max_length=50)


class BTPProject(models.Model):
	code = models.CharField(max_length=8)
	title = models.CharField(max_length=150)
	description = models.TextField(default='NA')
	supervisor = ArrayField(models.SmallIntegerField())
	postedby = models.ForeignKey(User)
	isfileuploaded = models.BooleanField(default=False)
	isexternal = models.BooleanField(default=False)
	fileuploaded = models.FileField(null=True,blank=True,upload_to='')
	display = models.BooleanField(default=True)
	def __str__(self):
		return str(self.code)+" "+str(self.title)
	


	
class BTPStudent(models.Model):
	user = models.OneToOneField(User)
	branch = models.CharField(max_length=5) 
	rollno = models.CharField(max_length=15)
	btpproject = models.ForeignKey(BTPProject)
	def __str__(self):
		return self.rollno
	def fullname(self):
		return self.user.get_full_name()

class Faculty(models.Model):
	user = models.OneToOneField(User)
	
	def __str__(self):
		return str(self.id)
	
	def fullname(self):
		return self.user.get_full_name()
	def get_all_projects(self):
		ProjectList = []
		btpprojects = BTPProject.objects.a()
		for btpro in btpprojects:
			if (self.user.id in btpro.supervisor):
				ProjectList.append(btpro)

		return ProjectList
 
class Semester(models.Model):
	name = models.CharField(max_length=15)
	sem = models.SmallIntegerField()
	batch = models.CharField(max_length=5,choices=choices.YEAR_BATCHES)
	year = models.DateField()
class BTPWeek(models.Model):
	weekno = models.PositiveIntegerField(default=0)
	startdate = models.DateTimeField()
	enddate = models.DateTimeField()
	def __str__(self):
		return str(self.weekno)
		

class BTPEvalPanel(models.Model):
	name = models.CharField(max_length=15)
	members = ArrayField(models.SmallIntegerField())
	def __str__(self):
		return str(self.name)
class BTPEvalGroup(models.Model):
	groupno = models.PositiveIntegerField(default=0)
	projects = ArrayField(models.SmallIntegerField())
	panel = models.ForeignKey(BTPEvalPanel)



class BTPSubmission(models.Model):
	week = models.ForeignKey(BTPWeek)
	project = models.ForeignKey(BTPProject)
	submitted_at = models.DateTimeField()
	fileuploaded = models.FileField(upload_to='/btp/evaluation/submissions/')
	submitted_by = models.ForeignKey(User)
	
