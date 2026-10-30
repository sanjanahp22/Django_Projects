from django.shortcuts import render


def home(request):
    return render(request,'myapp/static.html')

# Create your views here.
