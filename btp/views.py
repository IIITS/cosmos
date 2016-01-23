from btp.models import BTPStudent, Faculty, BTPProject, BTPSubmission
from btp.forms import LoginForm
from btp import methods
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.conf import settings
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

class IndexView(TemplateView):
	template_name = 'index/index.html'
	def get_context_data(self, **kwargs):
		context=super(IndexView,self).get_context_data(**kwargs)
		context = {'title':'Septem'}
		return context
	def dispatch(self, *args, **kwargs):
		return super(IndexView,self).dispatch(*args,**kwargs)
class BTPIndexView(TemplateView):
	template_name = 'btp/btpindex.html'
	def get_context_data(self, **kwargs):
		context=super(BTPIndexView,self).get_context_data(**kwargs)
		
		projects = BTPProject.objects.order_by('title')
		faculty = Faculty.objects.all()
		students = BTPStudent.objects.all()
		submissions = methods.get_submissions_currentweek()
		mysubmissions = BTPSubmission.objects.filter(submitted_by = self.request.user).order_by('submitted_at')
		
		context = {'title':'Home - BTP',
			   'students':students,
			   'faculty':faculty,
			   'submissions':submissions,
			   'mysubmissions':mysubmissions,
			   'projects':projects			
		}
		return context
	def dispatch(self, *args, **kwargs):
		return super(BTPIndexView,self).dispatch(*args,**kwargs)

class LoginView(FormView):
	template_name = 'accounts/login.html'
	form_class = LoginForm
	success_url = settings.LOGIN_REDIRECT_URL
	def form_valid(self,form):
		username = form.cleaned_data['username']
	    	password = form.cleaned_data['password']
    		user = authenticate(username=username, password=password)
		
    		if user is not None:
			
        		if user.is_active:
				
            			login(self.request, user)
			return HttpResponseRedirect(settings.LOGIN_URL)
		return super(LoginView,self).form_valid(form)
	def form_invalid(self,form):
		print "here"
		return super(LoginView,self).form_invalid(form)
	def get_context_data(self,**kwargs):	
		context = super(LoginView,self).get_context_data(**kwargs)
		context = {'title':'Login - Septem',
			   'form':LoginForm(self.request.POST)	
		}
		return context

class WeekScheduleView(TemplateView):
	template_name = 'index.html'
	def get_context_data(self, **kwargs):
		context = {'title':'Schedules - BTP'}
		return context
	def dispatch(self, *args, **kwargs):
		return super(WeekScheduleView,self).dispatch(*args,**kwargs)
class BTPSubmissionFormView(FormView):
	template_name = 'submit.html'
	def get_context_data(self, **kwargs):
		context = {'hello_txt':'Hello'}
		return context
	def dispatch(self, *args, **kwargs):
		return super(BTPSubmissionFormView,self).dispatch(*args,**kwargs)
class BTPSubmissionsView(TemplateView):
	template_name = 'submissions.html'
	def get_context_data(self, **kwargs):
		context = {'hello_txt':'Hello'}
		return context
	def dispatch(self, *args, **kwargs):
		return super(BTPSubmissionsView,self).dispatch(*args,**kwargs)	

class PasswordChangeView(TemplateView):
	template_name = 'submissions.html'
	def get_context_data(self, **kwargs):
		context = {'hello_txt':'Hello'}
		return context
	def dispatch(self, *args, **kwargs):
		return super(PasswordChangeView,self).dispatch(*args,**kwargs)	
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)

