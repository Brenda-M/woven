from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
  publisher = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  image = models.ImageField(upload_to='projects')
  link = models.URLField(max_length=200)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

  def __str__(self):
    return self.title

  def save_project(self):
    return self.save()

  

