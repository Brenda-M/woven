from django.db import models

class Project(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  image = models.ImageField(upload_to='projects')
  link = models.URLField(max_length=200)

  def __str__(self):
    return self.title

  def save_project(self):
    return self.save()

  

