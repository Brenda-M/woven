from django import forms
from .models import Project, Rating

class CreateNewForm(forms.ModelForm):

  class Meta:
    model = Project
    fields = ['title', 'description', 'image', 'link']

class RatingForm(forms.ModelForm):
  class Meta:
    model = Rating
    fields = ['design','usability', 'content']
