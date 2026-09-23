from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from django.contrib.auth import  authenticate, login, logout
import json
from .models import Employee
# Create your views here.
def hello(request):
  return JsonResponse({
    "message":"Hello App working"
  })

@csrf_exempt
def usersapi(request,username=None):
  if request.method == "GET":
    users = User.objects.values().all()

    return JsonResponse({
      "users":list(users)
    })

  elif request.method == "POST":
    data = json.loads(request.body)
    try:
      user = User.objects.create_user(**data)
      return JsonResponse({
        "message":"User created successfully",
        "data":data
      },status=201)
    except Exception as e:
      return JsonResponse({
        "message":"User not created",
      })

  elif request.method =="PUT":
    data = json.loads(request.body)

    try:
      user = User.objects.get(username=username)
      # user = User.objects.filter(username=username)
      user.email = data["email"]
      user.set_password(data["password"]) #django method to hash the password
      user.save()
      # user.update(**data)
      return JsonResponse({
        "message":"User updated Successfully",
        "data":data
      },status=201)
    except Exception as e:
      return JsonResponse({
        "message":"User not found",
        "Error":str(e)
      },status=403)

  elif request.method == "PATCH":
    data = json.loads(request.body)
    
    try:
      user = User.objects.get(username=username)
      if "email" in data:
        user.email = data["email"]
      if "first_name" in data:
        user.first_name = data["first_name"]
      user.save()
      return JsonResponse({
      "message":"User updated Successfully"
      },status=201)
    except Exception as e:
      return JsonResponse({
      "message":"User not found",
      "Error":str(e)
      },status=403)

  elif request.method == "DELETE":
    try:
      user = User.objects.get(username=username)
      user.delete()
      return JsonResponse({
        "message":"User deleted Successfully",
        "user":user.username
      },status=200)
    except Exception as e:
      return JsonResponse({
        "message":"User Not Found",
        "Error":str(e)
      },status=403)

def groupapi(request):
  groups = Group.objects.values().all()
  return JsonResponse({
    "groups":list(groups)
  })

@csrf_exempt
def login_user(request):
  if request.method == "POST":
    data = json.loads(request.body)
    username = data["username"]
    password = data["password"]
    user = authenticate(
      username = username,
      password = password
    )

    if user is None:
      return JsonResponse({
        "error":"Invalid username or password"
      },status = 401)

    login(request,user)
    return JsonResponse(
      {
        "msg":"login Successfull",
        "username":username,
        "email":user.email # we are accessing the email from user object also not passing it for the authentication
      })

def logout_user(request):
  username = request.user.username
  logout(request)
  return JsonResponse({
    "msg":"Logout Successfull",
    "Username":username
  },status=200)

def profile(request):

  if not request.user.is_authenticated:
    return JsonResponse(
      {
        "msg":"User not found"
      },status=401
    )

  return JsonResponse({
    "username":request.user.username, #to get the credentials from the session that we crated using login in the above api
    "email":request.user.email
  })

@csrf_exempt
def create_employee(request): #we using this api to perform operations only for who have loggedin
  if request.method=="POST":

    if not request.user.is_authenticated: #to check whether the user is logged in 
      return JsonResponse(
      {
        "msg":"Login Required"
      },status=401) 
    
    print(request.user.get_all_permissions())
    if not request.user.has_perm(
      "usersapp.add_employee"
    ):                                        # to check whther he has operational permission after loggedin
      return JsonResponse({
        "error": "You dont have permission"
      },status=403)

    

    data = json.loads(request.body)
    name = data["name"]
    email = data["email"]
    department = data["department"]

    emp = Employee.objects.create(
      name=name,
      email=email,
      department=department
    )

    return JsonResponse({
      "id":emp.id,
      "name":emp.name,
      "email":emp.email,
      "department":emp.department
    })


@csrf_exempt
def update_employee(request,name):
  if request.method=="PUT":
    if not request.user.is_authenticated: #to check whether the user is logged in 
      return JsonResponse(
      {
        "msg":"Login Required"
      },status=401) 
        
     
    if not request.user.has_perm(
      "usersapp.change_employee"
    ):                                        # to check whther he has operational permission after loggedin
      return JsonResponse({
        "error": "You dont have permission"
          },status=403)
    print(request.user.get_all_permissions())  
    data = json.loads(request.body)
    
    
    try:
      users = Employee.objects.get(name=name)
    except Employee.DoesNotExist:
      return JsonResponse({
        "error": "Employee not found"
    }, status=404)

    users.name = data["name"]
    #users.email = data["email"]
    users.department = data["department"]
    
    users.save()
    
    return JsonResponse({
      "id":users.id,
      "name":users.name,
      "email":users.email,
      "department":users.department
      })