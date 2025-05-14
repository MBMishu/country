from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse,FileResponse

from django.contrib.auth import authenticate, login, logout
from django.conf import settings

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User

import requests
from django.conf import settings

from .decorators import *
from api.models import *
from .forms import *


def home(request):
    api_url = f"{request.scheme}://{request.get_host()}/api/countries/"
    
    unique_country_names = set()
    unique_regions = set()
    total_population = 0
    total_area = 0
    total_independent_count = 0
    unique_languages = set()
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        countries = response.json()
        
        for country in countries:
            unique_country_names.add(country['name'])
            
            region = country.get('region')
            if region:
                unique_regions.add(region)
                
            total_population += country['population']
            total_area += country['area']
            total_independent_count += 1 if country['independent'] else 0
            
            for language in country.get('languages', []):
                if isinstance(language, dict):
                    name = language.get('name')
                    if name:
                        unique_languages.add(name)
                elif isinstance(language, str):
                    unique_languages.add(language)
        
        
        
    except requests.exceptions.RequestException as e:
        countries = []
        print(f"Error fetching countries: {e}")
    
    context = {
        'total_countries': len(unique_country_names),
        'total_regions': len(unique_regions),
        'total_population': total_population,
        'total_area': total_area,
        'total_independent': total_independent_count,
        'total_languages': len(unique_languages),
    }
    return render(request, 'dashboard/home.html', context)

def ListCountries(request):
    api_url = f"{request.scheme}://{request.get_host()}/api/countries/"
    print(api_url)
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        countries = response.json()
    except requests.exceptions.RequestException as e:
        countries = []
        print(f"Error fetching countries: {e}")
    
    context = {
        'countries': countries,
    }
    return render(request, 'dashboard/countries.html', context)

def SameRegionCountries(request, cca2):
    
    country_url = f"{request.scheme}://{request.get_host()}/api/country-details/{cca2}/"
    print(country_url)
    
    try:
        response = requests.get(country_url)
        response.raise_for_status()  # Raise an error for bad responses
        country = response.json()
    except requests.exceptions.RequestException as e:
        country = {}
        print(f"Error fetching country details: {e}")
        
   
    
    api_url = f"{request.scheme}://{request.get_host()}/api/same-region/{cca2}/"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        countries = response.json()
    except requests.exceptions.RequestException as e:
        countries = []
        print(f"Error fetching countries: {e}")
    
    context = {
        'country': country,
        'countries': countries,
    }
    return render(request, 'dashboard/countries-details.html', context)