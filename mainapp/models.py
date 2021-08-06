from django.db import models

# Create your models here.

class tab_register(models.Model):
    username=models.CharField(max_length=50)
    phone=models.CharField(max_length=12,null=True)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    status=models.CharField(max_length=10)
    gender=models.CharField(max_length=10,null=True)
    

class tab_login(models.Model):
    username2=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)
    status=models.CharField(max_length=10)