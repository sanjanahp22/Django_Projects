from django.db import models
# Create your models here.
class student (models.Model):
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=10)
    age=models.IntegerField()
    place=models.CharField(max_length=50)
    phonenum=models.CharField(max_length=10)
    dob=models.DateField()
    email=models.EmailField()
    
    # def __str__(self):
        # return self.name
    
    

