from django.shortcuts import render
from django.http import HttpResponse

def myview(request):
    return render(request,'myapp/index.html')


def myview1(request):
    return render(request,'myapp/index1.html')

def myview2(request):
    name='sanjana'
    age=22
    a=(f''my name is ',{name} 'and age is ',{age}')
    
    


   








   

# Create your views here.
