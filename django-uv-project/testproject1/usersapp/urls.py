from django.urls import path
from .views import hello, usersapi, groupapi,login_user,logout_user, profile, create_employee, update_employee
urlpatterns = [
    path("hello/",hello),
    path("/groups/",groupapi),
    path("/login_user/",login_user),
    path("/logout_user/",logout_user),
    path("/create_employee/",create_employee),
    path("/update_employee/<str:name>/",update_employee),
    path("/profile/",profile),
    path("/",usersapi),
    path("/<str:username>/",usersapi),
   

]