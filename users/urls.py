from django.urls import path
from . import views
from .views import ProfileList
 
urlpatterns = [
  path('profile/', views.profile, name='profile'),
  path('api/v1/profile', views.ProfileList.as_view()),
]