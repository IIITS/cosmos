from django.contrib.auth.models import User
from django.utils import timezone
from btp.models import *
WEEK_MAX = 4
def is_in_past(time):
	return timezone.now() > time
def is_in_future(time):
	return timezone.now() < time

def get_current_week():
	weeks = BTPWeek.objects.all()
	for week in weeks:
		if week.startdate <= timezone.now() and week.enddate >= timezone.now():
			return week.weekno
	return False


def get_submissions_currentweek():
	submissions = BTPSubmission.objects.all()
	SubList = []
	for btps in submissions:
		if btps.week.week.weekno == get_current_week():
			SubList.append(btps)
	return SubList

def check_faculty(user):
	fac = Faculty.objects.all()
	for f in fac:
		if f.user == user:
			return True
	return False

def getStudentIdByUser(user):
	try:
		student = BTPStudent.objects.get(user=user)
		return student.id
	except KeyError:
		return False
	return False
def getProjectGroupByStudentId(stid):
	try:	
		btpProjectGroup = BTPProjectGroup.objects.get(students__contains=[int(stid)])
		return btpProjectGroup
	except KeyError:
		return False
	return False

def getBTPEvalSetByProjectGroup(group):
	try:
		evalset = BTPEvalSet.objects.get(projectgroups__contains=[group.id])
		return evalset
	except KeyError:
		return False
	return False
def getAllBTPProjectGroupsByEvalSet(evalset):
	ProjectGroups = [] 
	pg_evalset = evalset.projectgroups
	for es in pg_evalset:
		btpgs = BTPProjectGroup.objects.get(id = es)
		ProjectGroups.append(btpgs)
	return ProjectGroups
    
def getUserTypes(user):
	USERTYPELIST = []
	facs = Faculty.objects.all()
	studs = BTPStudent.objects.all()
	for f in facs:
		if user == f.user:
			USERTYPELIST.append("FACULTY")	
			break
	for s in studs:
		if user == s.user:
			USERTYPELIST.append("STUDENT")	
			break
	return USERTYPELIST
def getCurrentWeek():
	weeks = BTPWeek.objects.all()
	for week in weeks:
    		if week.starttime <= timezone.now() and week.endtime >= timezone.now():
				return week
		elif week.starttime >= timezone.now():
				return BTPWeek.objects.get(weekno=1)
		elif week.endtime <= timezone.now():
				return BTPWeek.objects.get(weekno= WEEK_MAX)
	return 0

def getBTPSetWeek(sets, week):
	btpsetweek =BTPSetWeek.objects.get(sets=sets, week=week)
	return btpsetweek



