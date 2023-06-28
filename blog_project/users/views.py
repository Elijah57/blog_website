from django.shortcuts import render, redirect
from .form import UserRegForm, ProfileUpdateForm, UserUpdaterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
	if request.method == "POST":
		form = UserRegForm(request.POST)

		if form.is_valid():
			uname = form.cleaned_data.get("username")
			messages.success(request, f"Account successfully created for {uname}")
			form.save()

			return redirect("login")

	else:
		form = UserRegForm()

	return render(request, "users/register.html", context={"form": form})


@login_required(login_url="login") 
def profile(request):
	if request.method == "POST":
		user_form = UserUpdaterForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, f"Your account has been updated")
			return redirect('profile')

	else:
		user_form = UserUpdaterForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)
	
	context ={"user_form": user_form , "profile_form": profile_form}
	return render(request, "users/profile.html", context)



