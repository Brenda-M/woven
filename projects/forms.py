from django import forms
from .models import Project

class CreateNewForm(forms.ModelForm):

  class Meta:
    model = Project
    fields = ['title', 'description', 'image', 'link']
