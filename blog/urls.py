from django.urls import path, include
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [

    path('', PostListView.as_view(), name="home"),
    path("about/",views.about, name="about"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/update/<int:pk>/", PostUpdateView.as_view(), name="update-post"),
    path("post/delete/<int:pk>/", PostDeleteView.as_view(), name="delete-post"),
  
]

