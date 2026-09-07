from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.
def  home(request):
  return render(request,"home.html")

def about(request):
  return JsonResponse({"message":"Welcome to about section"})

def hello(request, name):
  return JsonResponse({"message":f"hello {name}"})

def welcome(request,name):
  return HttpResponse(f"""
                          <h1>Welcome {name}</h1>
                          <p> This is welcome page</p1>
                       """)
def welcome_home(request):
  return render(request,"home.html")

def profile(request,name):
  is_admin =True
  email = f"{name}@exmaple.com"
  return render(request, "profile.html",
                {"name": name , "email": email, "city": "Newyork", "is_admin": is_admin})