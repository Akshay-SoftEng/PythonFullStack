from rest_framework import serializers
from .models import Employee, Department

# class EmployeeSerializer(serializers.Serializer):  #regular serializers
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length = 100)
#     email = serializers.EmailField()
#     department = serializers.CharField(max_length=100)

class EmployeeSerializer(serializers.ModelSerializer): #Model Serialers
  department_name = serializers.SerializerMethodField()
  department_location = serializers.SerializerMethodField()
  class Meta:
    model = Employee
    fields = ["id", "name", "email", "department","department_name", "department_location"]

    read_only_fields = [
            "id"
        ]
    write_only_fields = [
        "email",
        "department"
    ]


    
    def validate_name(self,value):
        name = value.lower()#admin
        if name=="admin":
            raise serializers.ValidationError(
                "Admin is not a valid employee name"
            )
        return value
    
    def validate_email(self,value):
        email_prefix = value.split('@')[0]
        if email_prefix=="admin":
            raise serializers.ValidationError(
                f"{value} is not a valid employee email"
            )
        return value

  def get_department_name(self, obj):
    return obj.department.name
  
  def get_department_location(self, obj):
    return obj.department.location




class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
      model = Department
      fields = ["name", "location"]
    