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
		return str(self.rollno) +"   "+ str(self.user.get_full_name())
	def fullname(self):
		return self.user.get_full_name() 

class Faculty(models.Model):
	user = models.OneToOneField(User)
	
	def __str__(self):
		return str(self.user.get_full_name())
	
	def fullname(self):
		return self.user.get_full_name()
	def get_all_projects(self):
		ProjectList = []
		btpprojects = BTPProject.objects.all()
		for btpro in btpprojects:
			if (self.id in btpro.supervisor):
				ProjectList.append(btpro)

		return ProjectList
 
class Semester(models.Model):
	name = models.CharField(max_length=15)
	sem = models.SmallIntegerField()
	batch = models.CharField(max_length=5,choices=choices.YEAR_BATCHES)
	start = models.DateField() 
	end = models.DateField()
class BTPWeek(models.Model):
	weekno = models.PositiveIntegerField(default=0)
	starttime = models.DateTimeField()
	endtime = models.DateTimeField()
	def __str__(self):
		return "Week - "+str(self.weekno)
		

class BTPEvalPanel(models.Model):
	name = models.CharField(max_length=15)
	members = ArrayField(models.SmallIntegerField())
	def __str__(self):
		return str(self.name)


class BTPProjectGroup(models.Model):
	project = models.ForeignKey(BTPProject)
	students = ArrayField(models.SmallIntegerField())
	faculty = ArrayField(models.SmallIntegerField())
	def __str__(self):
		return self.project.code

class BTPEvalSet(models.Model):
	groupno = models.PositiveIntegerField(default=0)
	projectgroups = ArrayField(models.SmallIntegerField())
	panel = models.ForeignKey(BTPEvalPanel)
	def __str__(self):
		return "set  - "+str(self.groupno)

class BTPSetWeek(models.Model):
	sets = models.ForeignKey(BTPEvalSet)
	week = models.ForeignKey(BTPWeek)
	evalday = models.DateField(default=timezone.now())
	starttime = models.DateField()
	endtime = models.DateField()
	submitdeadline = models.DateTimeField()
	def __str__(self):
		return "Set - "+str(self.sets.groupno) + " Week -"+str(self.week.weekno)	
class BTPSubmission(models.Model):
	week = models.ForeignKey(BTPSetWeek)
	projectgroup = models.ForeignKey(BTPProjectGroup,null=True)
	submitted_at = models.DateTimeField(auto_now = True)
	fileuploaded = models.FileField(upload_to='/btp/evaluation/submissions/')
	submitted_by = models.ForeignKey(User)
	
