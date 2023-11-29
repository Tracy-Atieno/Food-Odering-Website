from django.contrib import admin
from userreg.models import Userregistration,bannerdesc
from userreg.models import Addreview

class register(admin.ModelAdmin):
    list_display=('name' ,'lname','email','gender','username','Image')


admin.site.register(Userregistration,register)



class banner(admin.ModelAdmin):
    list_display=('title','description')

admin.site.register(bannerdesc,banner)


class adureview(admin.ModelAdmin):
    list_display = ['ureview']
    

admin.site.register(Addreview,adureview)


    

# Register your models here.
