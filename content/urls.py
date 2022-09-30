from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view,name='profile'),
    path('home/', views.home_view,name='home'),
    
   
]