from django.db import models



class product(models.Model):
    Employeename=models.CharField(max_length=50)
    Employyeage=models.IntegerField()
    Employeerole=models.CharField(max_length=30)
    Employeesalary=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField() #because of huge space
    image=models.ImageField(upload_to='products/')

# Create your models here.

