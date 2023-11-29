from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=50)
    desc=models.CharField(max_length=50)
    image=models.ImageField(upload_to="image/",max_length=250,null=True,default=None)
    url=models.URLField(null=True)



# Create your models here.
