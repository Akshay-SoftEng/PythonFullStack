from django.urls import path
# from .views import EmployeeView, EmployeeListView, EmployeeRetrieveView, DepartmentListView, EmployeeCreateView,DepartmentCreateAPIView
# from .views import EmployeeListCreateView, DepartmentListCreateView, EmployeeUpdateView, EmployeeDeleteView, DepartmentDeleteView, DepartmentUpdateView, EmployeeUpdateDeleteView, DepartmentUpdateDeleteView
from .views import EmployeeListCreateView, DepartmentListCreateView, EmployeeCRUDView, DepartmentCRUDView, LoginView, LogoutView 

urlpatterns  =  [
  # path('/', EmployeeView.as_view()),
  # path('/<int:id>/', EmployeeView.as_view()),
  # path('/list/',EmployeeListView.as_view()),
  # path('/list/<int:pk>/',EmployeeRetrieveView.as_view()),
  # path('/deps/',DepartmentListView.as_view()),
  # path('/create/',EmployeeCreateView.as_view()),
  # path('/deps/create/',DepartmentCreateAPIView.as_view()),
  # path('/', EmployeeListCreateView.as_view(), name = "employees"),
  # path('/<int:pk>/',EmployeeUpdateView.as_view()),
  # path('/<int:pk>/delete/',EmployeeDeleteView.as_view()),
  # path('/<int:pk>/',EmployeeUpdateDeleteView.as_view()),
  path('/<int:pk>/',EmployeeCRUDView.as_view()),
  path('/', EmployeeCRUDView.as_view(), name = "employees"),


  path('/deps/',DepartmentListCreateView.as_view(), name="department"),
  # path('/deps/<int:pk>/',DepartmentUpdateView.as_view()),
  # path('/deps/<int:pk>/delete/',DepartmentDeleteView.as_view()),
  # path('/deps/<int:pk>/',DepartmentUpdateDeleteView.as_view()),
  path('/deps/<int:pk>/',DepartmentCRUDView.as_view()),
  path("/login/",LoginView.as_view()),
  path("/logout/",LogoutView.as_view())

]