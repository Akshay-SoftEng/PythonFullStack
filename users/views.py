from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import UserProfile

# Create your views here.
def  home(request):
   if request.session.get("is_registered"):
    return render(request,"home.html")
   return redirect(register)

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

def users(request):
    users = [
      "Akshay",
      "Potta",
      "Sheero",
      "hima"
    ]
    return render(request, "users.html", {"users":users})

def register(request):
  if request.method == "POST":
    name = request.POST["name"]
    email = request.POST["email"]

    request.session["is_registered"]=True
    request.session["name"]=name
    request.session["email"]=email

    print("Name:", name)
    print("email:", email)

    return render(request, 'home.html',{"name":name, "email":email})
  return render(request, 'register.html')


def session_exit(request):
  # request.session["is_registered"]=False
   request.session.flush()
   return redirect(register)

def get_users_data(request):
  data = UserProfile.objects.all()
  return JsonResponse({
          "Users":list(data.values())
    })

def get_user_data(request, id):
  data = UserProfile.objects.get(id=id)
 # return JsonResponse({
  #        "id":data.id,
    #      "Name":data.name,
     #     "email":data.email
 #   })
  return JsonResponse(data)