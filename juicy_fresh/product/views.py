from django.shortcuts import render

# Create your views here.

def test(r):
    return render(r,'test.html')