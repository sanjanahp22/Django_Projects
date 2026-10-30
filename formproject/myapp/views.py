from django.shortcuts import render
from myapp.forms import studentform
from django.http import HttpResponse

def formview(request):
    f=studentform()
    if request.method=='POST':
        f=studentform(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponse("<h1 style='color:red'>recorded successfully </h1>")
    d={'form':f}
    return render(request,'form.html',d)
    
    
    
    
    
    
    
    
    

# Create your views here.
