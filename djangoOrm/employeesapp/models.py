from django.db import models

# Create your models here.
class Department(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Project(models.Model):
  name = models.CharField(max_length=100)
  budget = models.DecimalField(
      max_digits=12,
      decimal_places=2
  )
  
  def __str__(self):
      return self.name

class Employee(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  salary = models.DecimalField(
    max_digits=10,
    decimal_places=2
  )
  department = models.ForeignKey(
    Department,
    on_delete=models.CASCADE,
    related_name = "employees"
  )
  projects = models.ManyToManyField(
    Project,
    related_name="employeeprojects",
    blank=True
  )
  joining_date = models.DateField()
  is_active= models.BooleanField(
    default = True
  )

  def __str__(self):
    return self.name

