from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Employee, Department, Project
from .serializers import EmployeeSerializer, DepartmentSerializer, ProjectSerializer
from rest_framework.response import Response
from django.db.models import Q,F, Count, Avg, Max, Min, Sum


class EmployeeListCreateView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get(self,request):
        # emps = Employee.objects.filter(name__startswith="ra")
        # emps = Employee.objects.filter(salary=50000)
        # emps = Employee.objects.filter(salary__lt=55000)
        # emps = Employee.objects.filter(salary__gt=55000)
        # emps = Employee.objects.filter(salary__range=(40000,60000))
        # the above condition is 40000<=salary<=60000 which includes the limit values in the condition
        # emps = Employee.objects.filter(joining_date__year=2025)
        # emps = Employee.objects.filter(joining_date__day=8) 
        # emps = Employee.objects.filter(joining_date__month=4)
        # emps = Employee.objects.filter(joining_date__gt="2026-07-01")
        # emps = Employee.objects.filter(department__name__startswith="H") 
        # checks department name using __ as it is a lookup for the table and checks the condition with startswith
        # emps = Employee.objects.filter(is_active=True)
        

        # emps = Employee.objects.filter(~Q(department__name="IT"))
        # F expressions
        # emps = Employee.objects.filter(
        #     salary__gt=F('bonus'),bonus__gt=0
        # )

        #  we usually use this way to add value to fields because we dont want unecessary db calls
        # emps = Employee.objects.update(
        #    salary=F('salary')+5000
        # ) 

        #annotate - to use single no value to be return for each coloumn we use it
        # emps = Employee.objects.annotate(
        #     project_count = Count('projects')
        # )
        # emps = Employee.objects.filter()

                #aggregate(one overall result)
        # emps = Employee.objects.aggregate(
        #     total = Count('id')
        # )
        # emps = Employee.objects.aggregate(
        #             avg_salary = Avg('salary')
        #         )
        # emps = Employee.objects.aggregate(
        #                     sum_salary = Sum('salary')
        #                 )
        # emps = Employee.objects.aggregate(
        #                 highest_salary = Max('salary')
        #             )
        # emps = Employee.objects.aggregate(
        #                         lowest_salary = Min('salary')
        #                     )
        # return Response(emps)



        #assignment - 22 Day
        # emps = Employee.objects.filter(joining_date__day=8) 
        # emps = Employee.objects.filter(id__in=[1,3,5,7]) 
        # emps = Employee.objects.filter(projects__budget__gt=5000000).distinct()
        # emps = Employee.objects.filter(salary__gt=60000,department__name="IT")
        # emps = Employee.objects.filter(Q(salary__gt=60000) & Q(department__name="IT"))
        # emps = Employee.objects.filter(Q(salary__gt=70000) | Q(department__name="HR"))
        # emps = Employee.objects.filter(~Q(department__name="IT"))
        # emps = Employee.objects.filter((Q(salary__gt=50000) | Q(department__name="HR")) & Q(is_active=True))
        # emps = Employee.objects.filter(salary__gt=F("bonus"),bonus__gt=0)
        # emps = Employee.objects.filter(department__name="IT").update(salary=F('salary')+5000)
        # emps = Employee.objects.filter(department__name="IT")
        # emps = Employee.objects.annotate(
        #     project_count = Count('projects')
        # ).filter(project_count__gt=1)
        # emps = Employee.objects.aggregate(
        #             avg_salary = Avg('salary')
        #         )
        # emps = Employee.objects.aggregate(
        #                     sum_salary = Sum('salary')
        #                 )
        # emps = Employee.objects.aggregate(
        #                 highest_salary = Max('salary')
        #             )
        # emps = Employee.objects.aggregate(
        #                         lowest_salary = Min('salary')
        #                     )
        # return Response(emps)
        # emp_s = EmployeeSerializer(emps,many=True)
        # return Response(emp_s.data)
        # deps = Department.objects.annotate(
        #     employee_count=Count('employees')
        # )
        deps = Department.objects.annotate(
            employee_count=Count('employees')
        ).filter(employee_count__gt=3)

        dep_s = DepartmentSerializer(deps,many=True)
        return Response(dep_s.data)

from rest_framework.views import APIView
class EmployeeAPIView(APIView):

    def get(self, request):

        result = Employee.objects.aggregate(
            total_employees=Count('id'),
            total_salary=Sum('salary'),
            average_salary=Avg('salary'),
            highest_salary=Max('salary'),
            lowest_salary=Min('salary')
        )

        return Response(result)