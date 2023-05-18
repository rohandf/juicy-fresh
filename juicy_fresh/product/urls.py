from django.urls import path
from . import views

urlpatterns = [
     #path('',views.about,name='prod'), #with recents
     path('',views.about2), #with caching
     path('cmt/',views.cmt,name='cmtsubmit'),
     path('like/',views.like,name='likepage'),
     path('autocmplt/',views.autocmplt,name='acmplt'),
]