from django.urls import path
from .views import EmployeeView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
  path("/",csrf_exempt(EmployeeView.as_view()), name ="employee-list"),
  path("/create/",csrf_exempt(EmployeeCreateView.as_view()), name= "employee-form"),
  path("/<int:pk>/update/",csrf_exempt(EmployeeUpdateView.as_view()),name="employee-update"),
  path("/<int:pk>/delete/", csrf_exempt(EmployeeDeleteView.as_view()),name="employee-delete")
]