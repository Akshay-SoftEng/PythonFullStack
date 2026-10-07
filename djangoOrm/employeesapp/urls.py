from django.urls import path
from .views import EmployeeListCreateView
urlpatterns = [
  path('/',EmployeeListCreateView.as_view(),name="employees"),
]