from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('xyz/',views.test),
    path('login/',views.loginpage),
    path('login/loginsub/',views.loginsub),
    path('register/',views.registerpage),
    path('register/registersub/',views.registersub)
]