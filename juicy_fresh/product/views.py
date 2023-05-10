from django.shortcuts import render, redirect
from .models import fruits, comment

# Create your views here.

def test(r):
    uc = r.GET['usercomment']
    un = r.GET['user']
    pid = r.GET['pid']
    obj = comment.objects.create(proid_id=pid, user=un, msg=uc, like=0)
    obj.save()
    return redirect('/product/?id='+pid)

def about(r):
    idnum = r.GET['id']
    obj = fruits.objects.get(id=idnum)
    return render(r,'about.html',{'fruit':obj})

def cmt(r):
    return render(r,'text.html')

def like(r):
    return render(r,'text.html')