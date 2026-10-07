from rest_framework import serializers
from .models import Employee, Department, Project

class DepartmentSerializer(serializers.ModelSerializer):
  employee_count = serializers.IntegerField(read_only = True)
  class Meta:
      model = Department
      fields = [
          "id", "name","employee_count"
      ]
        
class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
      model = Project
      fields = [
          "id","name","budget"
      ]
class EmployeeSerializer(serializers.ModelSerializer):

  #we use this below serializers top display the department and projects name in the emp table since they all are related
  #we also have other method to display the names in the views.py by using methodField method object
  department = DepartmentSerializer(read_only=True)
  projects = ProjectSerializer(many=True,read_only=True)
  project_count = serializers.IntegerField(read_only = True)
  
  class Meta:
      model = Employee
      fields = [
          "id",
          "name",
          "email",
          "department",
          "projects",
          "project_count",
          "salary",
          "bonus",
          "joining_date",
          "is_active"
      ]