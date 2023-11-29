from django.db import models

class Userregistration(models.Model):
    name=models.CharField(max_length=50)
    lname=models.CharField(max_length=30)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=20)
    username=models.CharField(max_length=20,primary_key=True)
    passw=models.CharField(max_length=50)
    Image=models.ImageField(upload_to="profile/",max_length=100,null=True)

class bannerdesc(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=150)

class Addreview(models.Model):
    ureview=models.CharField(max_length=100)
    
    
