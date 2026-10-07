from django.urls import path
from .views import EmployeeListCreateView, EmployeeAPIView
urlpatterns = [
  path('/',EmployeeListCreateView.as_view(),name="employees"),
  path('/api/',EmployeeAPIView.as_view(),name="aggregate"),
  
]