from django.contrib import admin
from myapp.models import student

class studentadmin(admin.ModelAdmin):
    list_display=['name','place','email']
    
admin.site.register(student,studentadmin,)

# Register your models here.
