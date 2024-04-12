from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]

class UserUpdaterForm(forms.ModelForm): #update the user infor username and email
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["username", "email", ]

class ProfileUpdateForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ["firstname", "lastname", "image", "bio"]
