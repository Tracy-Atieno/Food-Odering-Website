from django.http import HttpResponse
from django.shortcuts import render,redirect,HttpResponseRedirect
from userreg.models import Userregistration,bannerdesc,Addreview
from Products.models import Prouct
from Products.models import Features,Categories
from blogs.models import Blog

def first(request):
    a="Hello world"
    return HttpResponse(a)

def second(request):
    a=30
    b=40
    c=a+b
    return HttpResponse(c)

def index(request):
    
    try:
        a=request.session.get('username')
        
        name=request.POST.get('uname')
        passw=request.POST.get('passw')
        lg=Userregistration.objects.get(username=name)
        uname=lg.username
        pass2=lg.passw
        if uname==name and pass2==passw:
            print("you are logged in")
            request.session['username']=uname
            a=request.session.get('username')
            print(a)
          
            if a!= None:
                return HttpResponseRedirect('/Home')
            else:
                return HttpResponseRedirect('/')
           
           

        else:
            print("you have to register yourself first")
        # data={'login':login}
        
    except:
        pass
    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        pic=request.POST.get('pic')
        try:
           
            obj=Userregistration(name=name,lname=lname,email=email,gender=gender,username=uname,passw=passw,Image=pic)
            obj.save()

        except:
            pass


   
    return render(request,"register.html")
def logout(request):
    del request.session['username']
    return HttpResponseRedirect("/")

def home(request):
    pr=Prouct.objects.all()
    fr=Features.objects.all()
    cr=Categories.objects.all()
    ds=bannerdesc.objects.get(id=1)
    usr=Userregistration.objects.all()
    bl=Blog.objects.all()
    try:
        txt=request.GET.get("text")
        print(txt)
        sf=Addreview(ureview=txt)
        sf.save()

    except:
        pass

    review=Addreview.objects.all()





    

    a=request.session.get('username')
    if a == None:
        return HttpResponseRedirect("/")
    data={'pr':pr,'ab':a,'fr':fr,'cr':cr,'ds':ds,'user':usr,'rw':review,'bl':bl}
    
    return render(request,"index.html",data)

def social(request):
    return redirect("https://www.instagram.com/abhishek9z/")
