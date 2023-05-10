from django.urls import path
from . import views

urlpatterns = [
     path('',views.about),
     path('test/',views.test,name='testpage')
]