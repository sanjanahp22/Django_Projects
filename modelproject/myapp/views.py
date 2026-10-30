from django.shortcuts import render
from myapp.models import student

def  studentdata(request):
    s=student.objects.all()
    ctx={'stud':s}
    return render(request,'table.html',ctx)

# Create your views here.
