from django.urls import path
from . import views

urlpatterns = [
     path('',views.about,name='prod'),
     path('cmt/',views.cmt,name='cmtsubmit'),
     path('like/',views.like),
     path('autocmplt/',views.autocmplt,name='acmplt'),
]