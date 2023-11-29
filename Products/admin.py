from django.contrib import admin
from Products.models import Prouct,Features,Categories

class Products(admin.ModelAdmin):

    list_display=("ptitle",'pprice','p_image')

admin.site.register(Prouct,Products)

class Feature(admin.ModelAdmin):
    list_display=('title','desc','fea_img')

admin.site.register(Features,Feature)

class CategoryRegister(admin.ModelAdmin):
    list_display=('title','discount','img')

admin.site.register(Categories,CategoryRegister)



# Register your models here.
