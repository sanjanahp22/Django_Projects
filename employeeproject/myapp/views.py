from django.shortcuts import render

from myapp.models import *
def fun(request):
    a=product.objects.all()
    s={'emp':a}
    return render(request,'employee.html',s)

# Create your views here.
