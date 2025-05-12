import requests
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone



@api_view(['GET'])
def fetch_countries(request):
    url = 'https://restcountries.com/v3.1/all'
    response = requests.get(url)
    if response.status_code == 200:
        countries_data = response.json()
 
        for data in countries_data:
            name = data['name']['common']
            
            

        return JsonResponse({
            'countries': countries_data
        }, status=status.HTTP_200_OK)   
    else:
        return JsonResponse({'error': 'Failed to fetch countries'}, status=response.status_code)
    
