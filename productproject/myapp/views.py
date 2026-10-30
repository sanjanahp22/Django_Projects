from django.shortcuts import render
from myapp.models import *
def fun(request):
    a=product.objects.all()
    s={'prod':a}
    return render(request,'product.html',s)

