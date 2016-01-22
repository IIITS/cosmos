from django.forms import Form, CharField, FileField, TextInput, PasswordInput, FileInput
from django.contrib.auth.forms import AuthenticationForm
class LoginForm(AuthenticationForm):
	username = CharField(widget=TextInput(attrs={'placeholder':'Enter your email', 
						 'class':'mdl-textfield__input', 'id':'username'
												}))
	password = CharField(widget=PasswordInput(attrs={'placeholder':'Enter your password',
						     'class':'mdl-textfield__input', 'id':'password'
												}))
class SubmissionForm(Form):	
	fileuploaded=FileField(widget=FileInput(attrs={'placeholder':'Please upload a file',
												   'class':'form-control'
												}))



