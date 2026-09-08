from django.urls import include,path
from .views import home, about,hello,welcome,welcome_home, profile, users,register, session_exit, get_user_data, get_users_data
urlpatterns = [
  path("home/", home, name = "home"),
  path("about/", about),
  path("hello/<str:name>/",hello),
  path("welcome/<str:name>/",welcome),
  path("welcome/",welcome_home),
  path("profile/<str:name>/", profile),
  path("users/",users),
  path("register/",register, name="register"),
  path("exit/",session_exit, name="exit"),
  path("get_users/",get_users_data),
  path("get_user/<int:id>",get_user_data)
  ]