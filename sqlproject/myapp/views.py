from django.shortcuts import render
from myapp.models import *


def fun(request):
    s=student.objects.all()
    d={'stud':s}
    return render(request,'index.html',d)
# Create your views here.
