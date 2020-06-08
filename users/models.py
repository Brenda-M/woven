from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  prof_pic = models.ImageField(default='default.png', upload_to='profile_pictures')
  bio = models.TextField(max_length=250, blank=True)
  created_at = models.DateField(auto_now_add=True)
  update_at = models.DateField(auto_now=True)

  def __str__(self):
    return f'{self.user.username} Profile'


  #resizing images..not the most efficient
  

  
# the profile model has a one to one relationship with the users model. That is, one user can have only one profile and one profile can be assoiciated to only one user. This means we can access a profile associated with a user directly from the user. e.g >>> from django.contrib.auth.models import User >>> user = User.objects.filter(username='testUser').first() >>> user.profile output - <Profile: testUser Profile>. To get the users info we can string the initial command even further. e.g user.profile.prof_pic output -<ImageFieldFile: default.jpg>



