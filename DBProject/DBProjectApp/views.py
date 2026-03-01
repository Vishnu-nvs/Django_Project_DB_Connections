from django.shortcuts import render

from .models import Employe

# Create your views here.
def Emp_data(request):
    data=Employe.objects.all()
    return render(request,"home.html",context={"data":data})
