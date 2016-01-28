from django.contrib.auth.models import User
from django.utils import timezone
from btp.models import BTPWeek, BTPSubmission, Faculty, BTPSetWeek, BTPStudent, BTPProjectGroup
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
		if btps.week.weekno == get_current_week():
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
def checkIfAllowedBtpProjectSubmissionBySet(group, week):
		setweek = BTPSetWeek.objects.get(sets=sets, week=week)
		if groupweek.startdate() < timezone.now()  and groupweek.submitdeadline >= timezone.now():
			return True
		else: 
			return False

def getBtpProjectGroupByStudent(student):
		bpgrp = BTPProject.objects.all()
		for bpg in bpgrp:
			if student.id in bpg.students:
				return bpg
		return False 

