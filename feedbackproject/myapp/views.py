from django.shortcuts import render, redirect
from myapp.feedback import studentform
from django.http import HttpResponse

def formview(request):
    f=studentform()
    if request.method=='POST':
        f=studentform(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponse("<h1 style='color:red'>recorded successfully </h1>")
    d={'form':f}
    return render(request,'feedback.html',d)




