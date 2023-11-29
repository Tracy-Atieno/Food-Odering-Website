from django.contrib import admin
from blogs.models import Blog

class Show(admin.ModelAdmin):
    list_display=("title","desc","image","url")

admin.site.register(Blog,Show)

# Register your models here.
