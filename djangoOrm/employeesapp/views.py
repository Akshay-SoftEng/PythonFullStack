from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
# Create your views here.


class EmployeeListCreateView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get(self,request):
        # emps = Employee.objects.filter(name__startswith="ra")
        # emps = Employee.objects.filter(salary=50000)
        # emps = Employee.objects.filter(salary__lt=55000)
        emps = Employee.objects.filter(salary__gt=55000)
        # emps = Employee.objects.filter(salary__range=(40000,60000))
        # the above condition is 40000<=salary<=60000 which includes the limit values in the condition
        # emps = Employee.objects.filter(joining_date__year=2025)
        # emps = Employee.objects.filter(joining_date__month=4)
        # emps = Employee.objects.filter(joining_date__gt="2026-07-01")
        # emps = Employee.objects.filter(department__name__startswith="H") 
        # checks department name using __ as it is a lookup for the table and checks the condition with startswith
        emp_s = EmployeeSerializer(emps,many=True)
        return Response(emp_s.data)