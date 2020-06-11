from django import forms
from .models import Project, Rating

class CreateNewForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['image', 'title', 'link', 'description','country', 'tag']

