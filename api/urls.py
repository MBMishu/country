from django.contrib import admin
from django.urls import path , include
from django.contrib.auth import views as auth_views
from .views import *
from . import views

urlpatterns = [
   
    path('fetch-countries/', views.fetch_countries, name='fetch-countries'),
    path('countries/', views.CountryListView, name='country-list'),
    path('countries/<str:name>', views.CountryListView, name='country-list'),
    
    path('country-details/<str:cca2>', views.CountryDetailView, name='country-details'),

    path('same-region/<str:cca2>/', views.SameRegionCountriesView, name='same-region'),
    path('same-language/<str:language>/', views.CountriesByLanguageView, name='same-language'),
    
    
    path('countries/create/', views.create_country, name='create_country'),
    path('countries/<str:cca2>/delete/', views.delete_country, name='delete-country'),
]