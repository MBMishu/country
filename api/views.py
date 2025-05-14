import requests
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

from rest_framework import status
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone

from .models import *
from .serializers import *

@api_view(['GET'])
def fetch_countries(request):
    url = 'https://restcountries.com/v3.1/all'
    response = requests.get(url)
    if response.status_code == 200:
        countries_data = response.json()
 
        for data in countries_data:
            name = data['name']['common']
            
            country, created = Country.objects.get_or_create(
                name=name,
                defaults={
                    'official': data.get('name', {}).get('official'),
                    'cca2': data.get('cca2'),
                    'cca3': data.get('cca3'),
                    'ccn3': data.get('ccn3'),
                    'cioc': data.get('cioc'),
                    'independent': data.get('independent', False),
                    'status': data.get('status', 'officially-assigned'),
                    'un_member': data.get('unMember', False),
                    'region': data.get('region'),
                    'subregion': data.get('subregion'),
                    'latitude': data.get('latlng', [None, None])[0],
                    'longitude': data.get('latlng', [None, None])[1],
                    'landlocked': data.get('landlocked', False),
                    'area': data.get('area'),
                    'flag_emoji': data.get('flag'),
                    'population': data.get('population'),
                    'fifa': data.get('fifa'),
                    'startOfWeek': data.get('startOfWeek'),
                    'google_maps': data.get('maps', {}).get('googleMaps'),
                    'openstreet_maps': data.get('maps', {}).get('openStreetMaps'),
                }
            )
            
            print(f"Country: {name}, Created: {created}")
            
        
            for cap in data.get('capital', []):
                capital.objects.get_or_create(country=country, capital=cap)
                
            print(f"Capital: {cap}, Created: {created}")
                
            
            currencies = data.get('currencies', {})
            for code, currency in currencies.items():
                Currency.objects.get_or_create(
                    country=country,
                    code=code,
                    name=currency.get('name'),
                    symbol=currency.get('symbol')
                )
                
            print(f"Currency: {currency}, Created: {created}")
            
            # Languages
            languages = data.get('languages', {})
            for code, lang in languages.items():
                Language.objects.get_or_create(country=country, code=code, name=lang)
                
            print(f"Language: {lang}, Created: {created}")
                
            for border in data.get('borders', []):
                Border.objects.get_or_create(country=country, border_country_code=border)
                
            print(f"Border: {border}, Created: {created}")
                
            
            for tld in data.get('tld', []):
                TopLevelDomain.objects.get_or_create(country=country, domain=tld)
                
            print(f"Top Level Domain: {tld}, Created: {created}")
                
            for cont in data.get('continents', []):
                Continent.objects.get_or_create(country=country, name=cont)
            
            print(f"Continent: {cont}, Created: {created}")
            
            for time in data.get('timezones', []):
                Timezone.objects.get_or_create(country=country, name=time)
            
            print(f"Continent: {time}, Created: {created}")
                
            flags = data.get('flags', {})
            Flag.objects.get_or_create(
                country=country,
                png_url=flags.get('png'),
                svg_url=flags.get('svg'),
                alt_text=flags.get('alt')
            )
            print(f"Flag: {flags.get('alt')}, Created: {created}")
            
            coat = data.get('coatOfArms', {})
            CoatOfArms.objects.get_or_create(
                country=country,
                png_url=coat.get('png'),
                svg_url=coat.get('svg')
            )
            print(f"Coat of Arms: {coat.get('svg')}, Created: {created}")
            
            
            # Native Names
            
            native_names = data.get('name', {}).get('nativeName', None)

            if native_names:
                if isinstance(native_names, dict):
                    for lang_code, names in native_names.items():
                        native_name, created = NativeName.objects.get_or_create(country=country, name=lang_code,
                                                                                   official = names.get('official'),
                                                                                   common = names.get('common')
                                                                                   )
                        
                        print(f"Native Name: {names.get('official')}, Created: {created}")
                else:
                    print(f"Native Name is not a dictionary for country: {name}")
            else:
                print(f"No nativeName data found for country: {name}")

                
            idd_data = data.get('idd', {})
            if idd_data:
                idd, _ = Idd.objects.get_or_create(country=country, root=idd_data.get('root'))
                for suffix_value  in idd_data.get('suffixes', []):
                    suffix.objects.get_or_create(Idd=idd, suffix=suffix_value )
            
            print(f"IDD: {idd_data.get('root')}, Created: {created}")
            
            for alt in data.get('altSpellings', []):
                altSpellings.objects.get_or_create(country=country, alt_spelling=alt)
                
            print(f"Alt Spelling: {alt}, Created: {created}")
            
            demonyms = data.get('demonyms', {})
            for  names, values in demonyms.items():
                demonym, _ = Demonym.objects.get_or_create(country=country, name=names,f = values.get('f'), m = values.get('m'))
               
            print(f"Demonym: {names}, Created: {created}")
            
            
            translations = data.get('translations', {})
            for lang_code, trans in translations.items():
                translation, _ = Translation.objects.get_or_create(country=country, language=lang_code, 
                                                                    official=trans.get('official'),
                                                                    common=trans.get('common'))
                
            print(f"Translation: {lang_code}, Created: {created}")

            gini_data = data.get('gini', {})
            for year, value in gini_data.items():
                gini, _ = Gini.objects.get_or_create(country=country, year=year, value=value)
                
                
            print(f"Gini: {year}, Created: {created}")
                
            car_data = data.get('car', {})
            if car_data:
                car, _ = Car.objects.get_or_create(country=country, side=car_data.get('side'))
                for sign in car_data.get('signs', []):
                    CarSign.objects.get_or_create(car=car, sign=sign)
                    
            print(f"Car: {car_data.get('side')}, Created: {created}")
                    
            
            cap_info = data.get('capitalInfo', {}).get('latlng',[])
            if cap_info:
                capitalInfo.objects.get_or_create(country=country, lat = cap_info[0], lng = cap_info[1])
            else:
                capitalInfo.objects.get_or_create(country=country, lat = None, lng = None)
                
            print(f"Capital Info: {cap_info}, Created: {created}")

            # Postal Code
            postal = data.get('postalCode', {})
            if postal:
                PostalCode.objects.get_or_create(
                    country=country,
                    format=postal.get('format'),
                    regex=postal.get('regex')
                )
                
            print(f"Postal Code: {postal.get('format')}, Created: {created}")

        return JsonResponse({'message': 'Countries fetched and saved successfully'}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'error': 'Failed to fetch countries'}, status=response.status_code)



# search countries by name or list all countries
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def CountryListView(request,name=None):
    countries = Country.objects.all()
    
    if name:
        countries = countries.filter(Q(name__icontains=name) | Q(official__icontains=name) | Q(cca2__icontains=name))
    
    serializer = CountryListSerializer(countries, many=True)
     
    return Response(serializer.data, status=status.HTTP_200_OK)

# same region countries
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def SameRegionCountriesView(request, cca2):
    country = get_object_or_404(Country, cca2=cca2)
    same_region_countries = Country.objects.filter(region=country.region).exclude(cca2=cca2)
    serializer = CountryListSerializer(same_region_countries, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# countries by language
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def CountriesByLanguageView(request, language):
    countries = Country.objects.filter(
        Q(languages__name__icontains=language) | Q(languages__code__icontains=language)
    ).distinct()
    serializer = CountryListSerializer(countries, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# country details by cca2
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def CountryDetailView(request, cca2):
    country = get_object_or_404(Country, cca2=cca2)
    serializer = CountrySerializer(country)
    return Response(serializer.data, status=status.HTTP_200_OK)

# create new entry
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_country(request):
    if request.method == 'POST':
        serializer = CountryModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# update country
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_country(request, cca2):
    country = get_object_or_404(Country, cca2=cca2)
    serializer = CountryModelSerializer(country, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# delete country  
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_country(request, cca2):
    country = get_object_or_404(Country, cca2=cca2)
    country.delete()
    return Response({"detail": "Country deleted."}, status=status.HTTP_204_NO_CONTENT)
