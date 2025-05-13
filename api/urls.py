from django.contrib import admin
from django.urls import path , include
from django.contrib.auth import views as auth_views
from .views import *
from . import views

urlpatterns = [
   
    path('fetch-countries/', views.fetch_countries, name='fetch-countries'),
    path('countries/', views.CountryListView, name='country-list'),
    path('countries/<str:name>', views.CountryListView, name='country-list'),
]