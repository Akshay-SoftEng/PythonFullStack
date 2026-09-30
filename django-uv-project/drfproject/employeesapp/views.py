from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer

# Create your views here.
class EmployeeView(APIView):
  def get(self,request, id = None):
    if id is None:
      data = Employee.objects.all()
      serializer  = EmployeeSerializer(data, many = True)
      return Response(serializer.data)
    
    else:
      try:
        data = Employee.objects.get(id=id)
      except Exception as e:
        return Response(
          {
            "msg":str(e) 
          }
        )

    return Response(
      {
        "Data":data
      }
    )


  def post(self,request):
    # name= request.data.get("name")
    # email = request.data.get("email")
    # department = request.data.get("department")

    # data = Employee.objects.create(name=name, email=email, department= department)
    # data = Employee.objects.create(**request.data)

    serializer = EmployeeSerializer(data = request.data)

    if serializer.is_valid():
      data = Employee(**request.data)
      data.save()
      return Response(
            {
              "data":data.name
            },status= status.HTTP_201_CREATED)
      
    # try:
    #   #data.full_clean()
    #   data.save()
    # except Exception as e:
    #   return Response({
    #       "error":e
    #     },status=400)

    return Response(
      {
        "errors":serializer.errors
      },status= 400)


  def put(self,request,id):
    employee = Employee.objects.get(id=id)
    serializer = EmployeeSerializer(employee,data = request.data)
    

    if  serializer.is_valid():
      # employee = Employee.objects.get(id=id)
      # employee.name = request.data.get("name")
      # employee.email = request.data.get("email")
      # employee.department = request.data.get("department")
      # employee.save()
      employee = serializer.save()
      return Response(serializer.data)


    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self,request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()

    return Response(
      {
        "id":id,
        "msg":"Employee Deleted successfully"
      },status=status.HTTP_204_NO_CONTENT
    )


# class EmployeeListView(ListAPIView):
#   queryset = Employee.objects.all()
#   serializer_class = EmployeeSerializer

# class EmployeeRetrieveView(RetrieveAPIView):
#   queryset = Employee.objects.all()
#   serializer_class = EmployeeSerializer

# class DepartmentListView(ListAPIView):
#   queryset = Department.objects.all()
#   serializer_class = DepartmentSerializer

# class EmployeeCreateView(CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# class DepartmentCreateAPIView(CreateAPIView):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer

class EmployeeListCreateView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DepartmentListCreateView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer  

# class DepartmentUpdateView(UpdateAPIView):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer    
    
# class EmployeeUpdateView(UpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer  

# class EmployeeDeleteView(DestroyAPIView):  #both update and delete can be combined into single class
#    queryset = Employee.objects.all()

# class DepartmentUpdateView(UpdateAPIView):
#    queryset = Department.objects.all()

# class DepartmentDeleteView(DestroyAPIView):
#    queryset = Department.objects.all()

class DepartmentUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer    
    
class EmployeeUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer 


class DepartmentCRUDView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# we need to overwrite the has permission method in BasePermission class to check the permissions
# we also need to pass this class to the permissionclasses in employeecrudview class 
from rest_framework.permissions import BasePermission
class CanViewEmployee(BasePermission):
    def has_permission(self,request, view):
        print(request.user.is_authenticated)
        print(request.user.has_perm("employeesapp.view_employee"))
        return request.user.is_authenticated and request.user.has_perm("employeesapp.add_employee")

# we have added the default rest_framework authentication classes in settings.py 

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser  , DjangoModelPermissions 

# data wont be populated in the put form in webpage as Retrieve API view is not working alongside with ListAPI View same with the department as well
class EmployeeCRUDView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):  
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer 
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated,DjangoModelPermissions, CanViewEmployee]

    #it is to display the custom fields instead of ListView fields from the serializer 
    # def get(self, request, *args, **kwargs):
    #    return Response({
    #       "message":"I am customget"
    #    })


class LoginView(APIView):
  @csrf_exempt
  def post(self,request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(
      username=username,
      password=password
    )
    if user is None:
      return Response({
        "message":"Invalid username / password"
      },status=401)
    login(request,user)
    return Response({
      "message":"Login Successfull",
      "username":username
    })
    
class LogoutView(APIView):
  def get(self,request):
    username = request.data.get("username")
    logout(request)
    return Response({
        "message":"Logout successfull",
        "user":username
    })