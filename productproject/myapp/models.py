from django.db import models

class product(models.Model):
    name=models.CharField(max_length=50)
    brand=models.CharField(max_length=50)
    material=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField() #because of huge space
    image=models.ImageField(upload_to='products/')

# Create your models here.
