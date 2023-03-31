from django.db import models

# Create your models here.

class Thilak(models.Model):
    thilak_name=models.CharField(max_length=100,primary_key=True)
    time=models.DateTimeField()
    
class Chandhra(models.Model):
    thilak_name=models.ForeignKey(Thilak,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField()

class Nagisetty(models.Model):
    name=models.ForeignKey(Chandhra,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)