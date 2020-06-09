from django.urls import path
from rest_framework import routers
from .views import PostListView, PostDetailView, PostCreateView, ProjectList
from . import views

urlpatterns = [
  path('', PostListView.as_view(), name='homepage'), 
  path('inspiration/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
  path('new/post/', PostCreateView.as_view(), name='new-post'),
  path('api/v1/projects', views.ProjectList.as_view())
]