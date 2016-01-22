from django.conf.urls import url
from btp import views 
from django.conf import settings
from django.contrib.auth.views import password_reset, logout
from django.contrib.auth.decorators import login_required
urlpatterns = [
	url(r'^$', login_required(views.IndexView.as_view()), name='homepage'),
	url(r'btp/$', login_required(views.BTPIndexView.as_view()),name='btphomepage'),
	url(r'accounts/login/$', views.LoginView.as_view(),name='loginpage'),
	url(r'secure/changepassword$', views.PasswordChangeView.as_view(),name='loginpage'),
	url(r'accounts/signout/$', views.logout_view,name='logoutpage'),
	url(r'accounts/login/$', views.LoginView.as_view(),name='loginpage')
]
if settings.SERVE_MEDIA:
    urlpatterns += (
        url(r'media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
        url(r'static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, }),
)
