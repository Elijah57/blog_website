from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Posts
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q 

# Create your views here.

#function based views
def home(request):
	posts = Posts.objects.all()
	context = {"posts": posts}
	return render(request, "home.html", context)

def detail(request, pk):
	post = Posts.objects.get(id=pk)

	context = {"post": post}
	return render(request, "blog/detail.html", context )

def about(request):
	return render(request, "about.html")

def user_page(request):
	return render(request, "user_page.html")

#class based views
#ListView, DetailView, CreateView, UpdateView, DeleteView
#Mixins - 

class PostListView(ListView):
	#for listing all of the blog post

	model = Posts  #what model to query in prder to create a listview
	template_name = "home.html"  #<app>/<model>_<viewtype>.html
	context_object_name = "posts"
	ordering = ["-date_posted"]
	paginate_by = 4 

	# def get(self):
		

	# def get_queryset(self, request):
	# 	q = self.request.GET.get("q") if self.request.GET != None else""

	# 	return Posts.objects.filter(Q(title__icontains=q) | Q(author__username__icontains=q) |
	# 		Q(content__icontains=q))



class UserListView(ListView):
	#for listing all of the blog post of a user
	model = Posts  #what model to query in prder to create a listview
	template_name = "home.html"  #<app>/<model>_<viewtype>.html
	context_object_name = "posts"
	ordering = ["-date_posted"]
	paginate_by = 4

class PostDetailView(DetailView):
	#accessing the detail/displaying a post
	model = Posts
	template_name = "detail.html"  #<app>/<model>_<viewtype>.html
	context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
	#to create a Post object (CR operation)
	model = Posts
	template_name = "post_form.html" #<app>/<model>_<viewtype>.html
	fields = ["title", "content"] #fields to include

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	#to update a Post object (U operation)
	model = Posts
	template_name = "post_form.html" #<app>/<model>_<viewtype>.html
	fields = ["title", "thumbnail", "content"]

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True 

		return False

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	#to delete a Post object (D operation)
	model = Posts
	template_name = "delete.html" #<app>/<model>_<viewtype>.html
	context_object_name = "obj"

	def get_success_url(self):
		return reverse_lazy("home")
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True 

		return False




posts = [
	{	
	"title": "DC-Motors",
	"author": "Elijah Echekwu",
	"date_posted": "September 23 2022",
	"content": "Dc DC-Motors are motors that are used for Direct current/voltages"
	},

	{
	"title": "AC-Motors",
	"author": "Elijah Echekwu",
	"date_posted": "September 24 2022",
	"content": "Ac AC-Motors are motors that are used for Alternating current/voltages"
	}

]
#tutorials 
#Detail view which renders a "detail" view of an object
#ListView which render a list of objects, typically from a queryset and optionally paginates them

#generic editview (Formview, and model-specific view CreateView, UpdateView, DeleteView)