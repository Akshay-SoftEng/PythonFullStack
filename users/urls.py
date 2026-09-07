from django.urls import include,path
from .views import home, about,hello,welcome,welcome_home, profile
urlpatterns = [
  path("home/", home),
  path("about/", about),
  path("hello/<str:name>/",hello),
  path("welcome/<str:name>/",welcome),
  path("welcome/",welcome_home),
  path("profile/<str:name>/", profile)
]