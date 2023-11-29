from django.db import models

class Prouct(models.Model):
    ptitle=models.CharField(max_length=50)
    pprice=models.IntegerField()
    p_image=models.FileField(upload_to="products/", max_length=200, null=True)


class Features(models.Model):
    title=models.CharField(max_length=70)
    desc=models.CharField(max_length=100)
    fea_img=models.ImageField(upload_to="Features/",max_length=100,null=True)

class Categories(models.Model):
    title=models.CharField(max_length=40)
    discount=models.IntegerField()
    img=models.ImageField()



# Create your models here.

