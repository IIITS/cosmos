from django.contrib.auth.models import User
from django.utils import timezone
from btp.models import BTPWeek, BTPSubmission
def is_in_past(time):
	return timezone.now() > time
def is_in_future(time):
	return timezone.now() < time

def get_current_week():
	weeks = BTPWeek.objects.all()
	for week in weeks:
		if week.startdate <= timezone.now() and week.enddate >= timezone.now():
			return week.weekno
	return int(0)

def get_submissions_currentweek():
	submissions = BTPSubmission.objects.all()
	SubList = []
	for btps in submissions:
		if btps.week.weekno == get_current_week():
			SubList.append(btps)
	return SubList

