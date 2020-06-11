from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from rest_framework import status
from .serializers import ProjectSerializer, RatingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import ListView, DetailView, CreateView
from .models import Project, Rating
from .forms import CreateNewForm
from .permissions import IsAdminorReadOnly

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
    form.instance.publisher = self.request.user
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

  permission_classes = (IsAdminorReadOnly,)

class RatingsList(APIView):
  
  def get(self, request, pk, format=None):
    project = get_object_or_404(Project, pk=pk)
    project_ratings = project.rating_set.all()
    design_criteria = []
    usability_criteria = []
    content_criteria = []
    
    average = 0
    for vote in project_ratings:
      design_criteria.append(vote.design)
      usability_criteria.append(vote.usability)
      content_criteria.append(vote.content)

    
    print(sum)
    # proj_average = []
    # for rating in project_ratings:
    #   proj_average.append(rating.average)
    #   final_vote = mean(proj_average)
    # result = round(final_vote, 2)

    serializers = RatingSerializer(project_ratings, many=True)
    return Response(serializers.data)
  
  def post(self, request, pk, format=None):
    serializers = RatingSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

def search(request):
  template = 'projects/search.html'
  query = request.GET.get('q') 
  results = Project.objects.filter( Q(title__icontains=query) | Q(description__icontains=query) | Q(tag__icontains=query))  
  context ={
    'results':results,
    'term':query
  }
  return render(request, template, context)


  


  
  
  









 



