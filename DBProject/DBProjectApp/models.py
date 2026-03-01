from django.db import models

# Create your models here.
class Employe(models.Model):
    Emp_id=models.PositiveIntegerField()
    Emp_name=models.CharField(max_length=100)
    Emp_salary=models.FloatField()
