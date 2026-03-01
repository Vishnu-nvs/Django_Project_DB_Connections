from django.contrib import admin
from . models import Employe
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=["Emp_id","Emp_name","Emp_salary"]
admin.site.register(Employe,EmpAdmin)