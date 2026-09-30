from django.urls import path
from .views import hello, usersapi, groupapi,login_user,logout_user, profile, create_employee, update_employee,delete_employee
from django.views.decorators.csrf import csrf_exempt
from .ClassBasedViews import hello, UserApi, EmployeeView # groupapi,login_user,logout_user, profile, create_employee, update_employee

urlpatterns = [
    path("/hello/",hello),
    path("/groups/",groupapi),
    path("/login_user/",login_user),
    path("/logout_user/",logout_user),
    path("/create_employee/",create_employee),
    path("/update_employee/<str:name>/",update_employee),
    path("/delete_employee/<str:name>/",delete_employee),
    path("/profile/",profile),
    path("/UserApi/",csrf_exempt(UserApi.as_view())),
    path("/UserApi/<str:username>/",csrf_exempt(UserApi.as_view())), #i am accessing CBV using UserApi i the url pattern to isolate from views urls's pattern
    path("/employeeview/",csrf_exempt(EmployeeView.as_view())),
    path("/",usersapi),
    path("/<str:username>/",usersapi),
   

]