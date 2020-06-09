from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from .serializers import ProjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
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

class ProjectList(APIView):
  def get(self, request, format=None):
    all_projects = Project.objects.all()
    serializers = ProjectSerializer(all_projects, many=True)
    return Response(serializers.data)
  
  def post(self, request, format=None):
    serializers = ProjectSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
  









 



