from django.shortcuts import render,redirect
from django.contrib import auth

# Create your views here.

def index(request):
    return render(request,'index.html')

def test(r):
    return render(r,'test.html',{'val':'java'})

def loginpage(r):
    return render(r,'login.html')

def registerpage(r):
    return render(r,'register.html')

def loginsub(request):
    uname = request.GET['uname']
    pword = request.GET['pword']
    user = auth.authenticate(username=uname,password=pword)
    if user:
        auth.login(request,user)
        return redirect('/')
    return render(request,'test.html',{'val':uname})

def registersub(request):
    uname = request.GET['uname']
    fname = request.GET['fname']
    lname = request.GET['lname']
    email = request.GET['email']
    pword = request.GET['pword']
    rpword = request.GET['rpword']

    return render(request,'test.html',{'val':uname})