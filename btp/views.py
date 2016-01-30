from btp.models  import *
from btp.forms   import *
from btp.methods import *

from django.core.exceptions import *
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.conf import settings
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login, update_session_auth_hash

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.decorators import login_required
from django.shortcuts import resolve_url
from django.template.response import TemplateResponse

class IndexView(TemplateView):
	template_name = 'index/index.html'
	def get_context_data(self, **kwargs):
		context=super(IndexView,self).get_context_data(**kwargs)
		context = {'title':'Cosmos'}
		return context
	def dispatch(self, *args, **kwargs):
		return super(IndexView,self).dispatch(*args,**kwargs)
class BTPIndexView(TemplateView):
	template_name = 'btp/btpindex.html'
	def post(self, request, *args, **kwargs):
		form = SubmissionForm(self.request.FILES, self.request.POST)
		print self.request.FILES['fileuploaded']
                fileuploaded = self.request.FILES['fileuploaded']
		currweek = getCurrentWeek()
		pg = getProjectGroupByStudentId(getStudentIdByUser(self.request.user))
		evalset = getBTPEvalSetByProjectGroup(pg)
		try:
				week = BTPSetWeek.objects.get(week = currweek, sets=evalset)
				submit = BTPSubmission( week = week , projectgroup = pg, fileuploaded = fileuploaded, submitted_by = self.request.user )
				submit.save()
				return HttpResponse({"posted":"True"})
		except ObjectDoesNotExist as error:
				week = BTPSetWeek.objects.all()[0]
		return JsonResponse({"posted":"False"})
	def get_context_data(self, **kwargs):
		context=super(BTPIndexView,self).get_context_data(**kwargs)
		
		projects = BTPProject.objects.order_by('title')
		faculty = Faculty.objects.order_by('user__first_name')
		is_faculty = check_faculty(self.request.user)
		students = BTPStudent.objects.order_by('rollno')
		#submissions = get_submissions_currentweek()
		mysubmissions = BTPSubmission.objects.filter(submitted_by = self.request.user).order_by('submitted_at')
		sets = getBTPEvalSetByProjectGroup( getProjectGroupByStudentId(getStudentIdByUser(self.request.user)) )
		week = getCurrentWeek()
		btpsetweek = getBTPSetWeek(sets, week)
		context = {'title':'Home - BTP',
			   'students':students,
			   'faculty':faculty,
			   #'submissions':submissions,
			   'mysubmissions':mysubmissions,
			   'btpsetweek':btpsetweek, 	
			   'projects':projects,
			   'header':'B-Tech Projects Portal',
                           'submissionsform':SubmissionForm(self.request.FILES, self.request.POST)		
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


@sensitive_post_parameters()
@csrf_protect
@login_required
def password_change(request,
                    template_name='accounts/password_change_form.html',
                    post_change_redirect = None,
                    password_change_form=ChangePasswordForm,
                    extra_context=None):
    if post_change_redirect is None:
        post_change_redirect = reverse('password_change_done')
    else:
        post_change_redirect = resolve_url(post_change_redirect)
    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(post_change_redirect)
    else:
        form = password_change_form(user=request.user)
    context = {
        'form': form,
        'title': ('Password change'),
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)
	
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)

class UnderConstruction(TemplateView):
	template_name = 'index/underconstruction.html'
	def dispatch(self, *args, **kwargs):
		return super(UnderConstruction,self).dispatch(*args, **kwargs)

