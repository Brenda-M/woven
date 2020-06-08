from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views

urlpatterns = [
  path('', PostListView.as_view(), name='homepage'), 
  path('inspiration/<int:pk>/', PostDetailView.as_view(), name='post-detail')
  path('new/post/', PostCreateView.as_view(), name='new-post')
]