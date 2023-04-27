from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User 

# Create your views here.

def index(request):
    return render(request,'index.html')

def test(r):
    return render(r,'test.html',{'val':'java'})

def login(request):
    if request.method=='POST':
        uname = request.POST['uname']
        pword = request.POST['pword']
        user = auth.authenticate(username=uname,password=pword)
        if user:
            auth.login(request,user)
            return redirect('/')
        msg = "Invalid username and password"
        return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pword = request.POST['pword']
        rpword = request.POST['rpword']
        if pword == rpword:
            if User.objects.filter(username=uname):
                msg = "Username is already taken"
                return render(request,'register.html',{'msg':msg})
            elif User.objects.filter(email=email):
                msg = "E-mail is already registered"
                return render(request,'register.html',{'msg':msg})
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,password=pword,username=uname,email=email)
                user.save();
                auth.login(request,user)
                return redirect('/')
        else:
            msg = "Passwords do not match"
            return render(request,'register.html',{'msg':msg})
    else:
        return render(request,'register.html')