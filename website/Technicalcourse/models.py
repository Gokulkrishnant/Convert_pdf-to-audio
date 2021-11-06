from django.db import models

# Create your models here.
class Allcourses(models.Model):
    coursename=models.CharField(max_length=200)
    instname=models.CharField(max_length=150)
class details(models.Model):
    course=models.ForeignKey(Allcourses,on_delete=models.CASCADE)
    sp=models.CharField(max_length=100)
    il=models.CharField(max_length=500)

