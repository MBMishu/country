from django.contrib import admin
from django.urls import path , include
from django.contrib.auth import views as auth_views

from . import views
from .views import *

urlpatterns = [
    path('', views.home, name="home"),
    path('countries/', views.ListCountries, name="ListCountries"),
    
    path('countries-similar/<str:cca2>/', views.SameRegionCountries, name="SameRegionCountries"),
    
     path('login/', views.HandleLogin, name="HandleLogin"),
    path('logout/', views.HandleLogout, name="HandleLogout"),
    path('register/', views.HandleRegister, name="HandleRegister"),
]