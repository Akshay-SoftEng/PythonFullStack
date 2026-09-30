from django.db import models

# Create your models here.
class Department(models.Model):
  name = models.CharField(max_length = 100, unique = True)    #we should define the department table above the employee as we have the foreignkey for this table
  location = models.CharField(max_length = 100)

  def __str__(self):
    return self.name

class Employee(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  # department = models.CharField(max_length= 100)
  department = models.ForeignKey(
    Department, on_delete=models.CASCADE, related_name="employees"
  )

  def __str__(self):
    return self.name


