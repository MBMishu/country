from rest_framework import serializers
from .models import *
        
class CountrySerializer(serializers.ModelSerializer):
    
    nativeName = serializers.SerializerMethodField()
    tld = serializers.SerializerMethodField()
    currency = serializers.SerializerMethodField()
    
    idd = serializers.SerializerMethodField()
    capital = serializers.SerializerMethodField()
    altSpellings = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()
    
    borders = serializers.SerializerMethodField()
    
    demonyms = serializers.SerializerMethodField()
    translations = serializers.SerializerMethodField()
    gini  = serializers.SerializerMethodField()
    car = serializers.SerializerMethodField()
    timezones = serializers.SerializerMethodField()
    continents = serializers.SerializerMethodField()
    
    flags = serializers.SerializerMethodField()
    coatOfArms = serializers.SerializerMethodField()
    capitalInfo = serializers.SerializerMethodField()
    postalCode = serializers.SerializerMethodField()
    
    def get_flags(self, obj):
        flags = obj.flag.all()
        if not flags:
            return []
        result = {}
        for data in flags:
            result['png'] = data.png_url
            result['svg'] = data.svg_url
            result['alt'] = data.alt_text
        return result
    
    def get_coatOfArms(self, obj):
        coat_of_arms = obj.coat_of_arms.all()
        if not coat_of_arms:
            return []
        result = {}
        for data in coat_of_arms:
            result['png'] = data.png_url
            result['svg'] = data.svg_url
        return result
    
    def get_capitalInfo(self, obj):
        capital_info = obj.capital_info.all()
        if not capital_info:
            return []
        result = {}
        for data in capital_info:
            result['latlng'] = data.lat , data.lng
        return result
    
    def get_postalCode(self, obj):
        postal_code = obj.postal_codes.all()
        if not postal_code:
            return []
        result = {}
        for data in postal_code:
            result['format'] = data.format
            result['regex'] = data.regex
        return result
    
    
    def get_continents(self, obj):
        continents = obj.continents.all()
        if not continents:
            return []
        return [data.name for data in continents]
    
    
    def get_timezones(self, obj):
        timezones = obj.timezones.all()
        if not timezones:
            return []
        return [data.name for data in timezones]
    
    
    def get_car(self, obj):
        car = obj.cars.all()
        if not car:
            return []
        result = {}
        for data in car:
            result['side'] = data.side
            result['signs'] = [sign.sign for sign in data.car_sign.all()]
        return result
    
    def get_gini(self, obj):
        gini = obj.gini.all()
        if not gini:
            return []
        result = {}
        for data in gini:
            result[data.year] = data.value
        return result
    
    def get_translations(self, obj):
        translations = obj.translations.all()
        if not translations:
            return []
        result = {}
        for data in translations:
            result[data.language] = {
                "official": data.official,
                "common": data.common
            }
        return result
    
    def get_demonyms(self, obj):
        demonym = obj.demonyms.all()
        if not demonym:
            return []
        result = {}
        for data in demonym:
            result[data.name] = {
                "f": data.f,
                "m": data.m
            }
        return result
    
    def get_borders(self, obj):
        borders = obj.borders.all()
        if not borders:
            return []
        
        return [data.border_country_code for data in borders]
    
    def get_languages(self, obj):
        languages = obj.languages.all()
        if not languages:
            return []
        result = {}
        for lang in languages:
            result[lang.code] = lang.name
        return result
    
    def get_altSpellings(self, obj):
        alt_spellings = obj.alt_spellings.all()
        if not alt_spellings:
            return []
        return [data.alt_spelling for data in alt_spellings]
    
    def get_capital(self, obj):
        capitals = obj.capitals.all()
        if not capitals:
            return []
        return [data.capital for data in capitals]
    
    def get_idd(self, obj):
        idd = obj.idds.all()
        if not idd:
            return []
        result = {}
        for idd_obj in idd:
            result['root']  = idd_obj.root
            result['suffix'] = [suffix.suffix for suffix in idd_obj.suffixes.all()]
            
        return result
    
    def get_nativeName(self, obj):
        native_names = obj.native_names.all()
        result = {}
        for native in native_names:
            result[native.name] = {
                "official": native.official,
                "common": native.common
            }
        return result
    
    def get_tld(self, obj):
        tlds = obj.tlds.all()
        if not tlds:
            return []
        return [tld.domain for tld in tlds]
    
    def get_currency(self, obj):
        currencies = obj.currencies.all()
        result = {}
        for currency in currencies:
            result[currency.code] = {
                "name": currency.name,
                "symbol": currency.symbol
            }
        return result

    class Meta:
        model = Country
        # fields = ['name', 'official','nativeName','tld',
        #           'cca2', 'ccn3', 'cioc', 'independent','status','un_member','currency',
        #           'idd','capital','altSpellings','region',
        #           'subregion','languages','latitude','longitude','landlocked','borders','area',
        #           'demonyms','cca3','translations','flag_emoji','google_maps','openstreet_maps','population',
        #           'gini','fifa','car','timezones','continents',
        #           'flags','coatOfArms','startOfWeek','capitalInfo','postalCode'
        #           ]
        fields = ['name', 'official','nativeName','tld',
                  'cca2', 'cca3', 'cioc', 'independent','status','un_member','currency',
                  'idd','capital','alt_spellings_values','region',
                  'subregion','languages_value','latitude','longitude','landlocked','borders_value',
                  'area','demonym','cca3','translations_value','flag_emoji',
                  'google_maps','openstreet_maps','population','gini_value',
                  'fifa','car','timezones_value','continent',
                  'flag_value','coat_of_arms_value','startOfWeek','capital_info_value','postal_code',
                  ]
        

    
        