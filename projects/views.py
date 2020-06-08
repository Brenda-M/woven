from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Project

class PostListView(ListView):
  projects = Project.objects.all()
  model = Project
  template_name = 'projects/main.html'
  context_object_name = 'projects'
  ordering = ['-id']



