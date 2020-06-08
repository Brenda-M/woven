from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ProjectSerializer
from django.views.generic import ListView, DetailView, CreateView
from .models import Project
from .forms import CreateNewForm

class PostListView(ListView):
  
  model = Project
  template_name = 'projects/main.html' #template convention is <app>/<model>_<viewtype>.html
  context_object_name = 'projects'
  ordering = ['-id']

class PostDetailView(DetailView):
  model = Project
  template_name = 'projects/post_detail.html'
  context_object_name = 'project'

class PostCreateView(CreateView):
  model = Project
  form_class = CreateNewForm
  template_name = 'projects/new_post.html'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ProjectViewSet(viewsets.ModelViewSet):
  queryset = Project.objects.all().order_by('- created_at')
  serializer_class = ProjectSerializer







 



