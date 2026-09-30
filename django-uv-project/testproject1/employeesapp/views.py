from django.shortcuts import render
from .models import Employee
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy #it's for redirecting to the template using urls
import json

# Create your views here. This is class based view
# class EmployeeView(View): #we using this api to perform CRUD operations only for who have loggedin and have permissions by CBV

#   def get(self,request):
#     emps = Employee.objects.values().all()
#     return JsonResponse(
#       {
#         "data":list(emps)
#       }
#     )
#   @csrf_exempt
#   def post(self,request):
#     data = json.loads(request.body)
#     name = data["name"]
#     email = data["email"]
#     department = data["department"]

#     emp = Employee.objects.create(
#       name=name,
#       email=email,
#       department=department
#     )
#     return JsonResponse({
#       "id":emp.id,
#       "name":emp.name,
#       "email":emp.email,
#       "department":emp.department
#     })

class EmployeeView(ListView): # Generic CBViews
  model = Employee # it is get view with internal implenetation we dont have to do it manually

class EmployeeCreateView(CreateView):
  model = Employee
  fields = [ 
    "name", "email", "department"
  ]
  template_name = "employeesapp/employee_form.html"
  success_url = reverse_lazy("employee-list") # generally we call the success_url by url but here we calling it by url's name so we use reverse_lazy here


class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = [
            "name",'email', 'department'
        ]
    template_name = "employeesapp/employee_form.html"
    success_url = reverse_lazy("employee-list")


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "employeesapp/employee_delete_confirmation.html"
    success_url = reverse_lazy("employee-list")