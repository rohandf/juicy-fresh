from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def test(r):
    return render(r,'test.html',{'val':'java'})