from django.shortcuts import render

def view3(request):
    name="sanjana"
    age=22
    place="Bengaluru"
    ctx={'name':name,'age':age,'place':place}
    return render(request,'jinja.html',ctx)

# Create your views here.
