import math
from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator

class Project(models.Model):
  publisher = models.ForeignKey(User, on_delete=models.CASCADE)
  tag = models.CharField(max_length=50, blank=True, null=True)
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  image = models.ImageField(upload_to='projects')
  link = models.URLField(max_length=200)
  country = models.CharField(max_length=100)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

  def __str__(self):
    return self.title

  def save_project(self):
    return self.save()

  def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk': self.pk})


class Rating(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  design = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
  content = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
  usability = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])

  def __str__(self):
    return f'{self.user.username} Votes'
    
  @classmethod
  def get_project_ratings(cls, projectid):
    ratings = cls.objects.filter(project = projectid)
    return ratings
  
  def individual_average(self):
    average = (self.design + self.content + self.usability)/3
    return average
  
  def votes_average(pk):
    ratings = Rating.get_project_ratings(pk)
    proj_average = []
    for rating in ratings:
      proj_average.append(rating.average)
      final_vote = mean(proj_average)
      return round(final_vote, 2)


  




  

