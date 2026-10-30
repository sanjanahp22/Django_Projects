from django.db import models
# Create your models here.
class  student(models.Model):
    name=models.CharField(max_length=50)
   
    email=models.EmailField()
  
    message = models.TextField()

    
    
# Create your models here.
