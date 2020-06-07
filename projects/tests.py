from django.test import TestCase
from .models import Project

class ProjectTestClass(TestCase):

  def setUp(self):
    self.project_1 = Project(title='Test Title', description='This is a test class for the project model', image='test.jpg', link='www.testimage.com')

  def test_save(self):
    return self.project_1.save_project()
  


