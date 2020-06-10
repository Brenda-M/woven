from django.db import models
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


#   #resizing images..not the most efficient
  
  def save(self, *args, **kwargs):
    super(Profile, self).save(*args, **kwargs)

    img = Image.open(self.prof_pic.path)
    if img.height> 300 or img.width > 300:
      output_size = (300, 300)
      img.thumbnail(output_size)
      img.save(self.prof_pic.path)




