from rest_framework import serializers
from .models import *



class CapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = capital
        fields = ['capital']


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['code', 'name', 'symbol']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['code', 'name']
        
class BorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Border
        fields = ['border_country_code']
        
class TimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timezone
        fields = ['name']
        
class TopLevelDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopLevelDomain
        fields = ['domain']
        
class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = ['name']
        
class FlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flag
        fields = ['png_url', 'svg_url', 'alt_text']
        
class CoatOfArmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoatOfArms
        fields = ['png_url', 'svg_url']
        
class DemonymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demonym
        fields = ['name', 'f', 'm']
        
class PostalCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostalCode
        fields = ['format', 'regex']
        
class SuffixSerializer(serializers.ModelSerializer):
    class Meta:
        model = suffix
        fields = ['suffix']
        
class IddSuffixSerializer(serializers.ModelSerializer):
    suffix = SuffixSerializer(many=True)
    
    class Meta:
        model = Idd
        fields = ['root', 'suffix']

class AltSpellingSerializer(serializers.ModelSerializer):
    class Meta:
        model = altSpellings
        fields = ['alt_spelling']
        
class TranslationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ['language', 'official', 'common']
        
class GiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gini
        fields = ['year', 'value']
        
class CapitalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = capitalInfo
        fields = ['lat', 'lng']
        
class CarSignSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSign
        fields = ['sign']
        
class CarSerializer(serializers.ModelSerializer):
    sign = CarSignSerializer(many=True)
    
    class Meta:
        model = Car
        fields = ['side', 'sign']

class NativeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = NativeName
        fields = ['name', 'official', 'common']
        
        
class CountryModelSerializer(serializers.ModelSerializer):
    capital = CapitalSerializer(many=True, write_only=True)
    currency = CurrencySerializer(many=True, write_only=True)
    language = LanguageSerializer(many=True, write_only=True)
    border = BorderSerializer(many=True, write_only=True)
    timezone = TimezoneSerializer(many=True, write_only=True)
    tld = TopLevelDomainSerializer(many=True, write_only=True)
    continent = ContinentSerializer(many=True, write_only=True)
    flags = FlagSerializer(many=True, write_only=True)
    coat_of_arm = CoatOfArmsSerializer(many=True, write_only=True)
    demonym = DemonymSerializer(many=True, write_only=True)
    postal_code = PostalCodeSerializer(many=True, write_only=True)
    idd = IddSuffixSerializer(many=True, write_only=True)
    alt_spelling = AltSpellingSerializer(many=True, write_only=True)
    translation = TranslationsSerializer(many=True, write_only=True)
    ginis = GiniSerializer(many=True, write_only=True)
    car = CarSerializer(many=True, write_only=True)
    native_name = NativeNameSerializer(many=True, write_only=True)
    capital_infos = CapitalInfoSerializer(many=True, write_only=True)
  
    
    
    class Meta:
        model = Country
        fields = ['name', 'official', 'native_name', 'tld', 'cca2', 'ccn3', 'cioc', 'independent', 'status', 'un_member',
                  'currency', 'idd', 'capital', 'alt_spelling', 'region', 'subregion', 'language', 'latitude',
                  'longitude', 'landlocked', 'border', 'area', 'demonym', 'cca3', 'translation', 'flag_emoji',
                  'google_maps', 'openstreet_maps', 'population', 'ginis', 'fifa', 'car', 'timezone', 'continent',
                  'flags', 'coat_of_arm', 'startOfWeek', 'postal_code',
                  'capital_infos'
                  ]
        
    def __init__(self, *args, **kwargs):
        if kwargs.get('partial', False):
            raise serializers.ValidationError("Partial updates are not allowed. Use PUT with complete data.")
        super().__init__(*args, **kwargs)
    def create(self, validated_data):
        native_name_data = validated_data.pop('native_name', [])
        tld_data = validated_data.pop('tld', [])
        currency_data = validated_data.pop('currency', [])
        idd_data = validated_data.pop('idd', [])
        car_data = validated_data.pop('car', [])
        capital_data = validated_data.pop('capital', [])
        alt_spelling_data = validated_data.pop('alt_spelling', [])
        language_data = validated_data.pop('language', [])
        border_data = validated_data.pop('border', [])
        demonym_data = validated_data.pop('demonym', [])
        translation_data = validated_data.pop('translation', [])
        ginis_data = validated_data.pop('ginis', [])
        timezone_data = validated_data.pop('timezone', [])
        continent_data = validated_data.pop('continent', [])
        flags_data = validated_data.pop('flags', [])
        coat_of_arm_data = validated_data.pop('coat_of_arm', [])
        postal_code_data = validated_data.pop('postal_code', [])
        capital_infos_data = validated_data.pop('capital_infos', [])

        country = Country.objects.create(**validated_data)

        for native in native_name_data:
            NativeName.objects.create(country=country, **native)
        for tld in tld_data:
            TopLevelDomain.objects.create(country=country, **tld)
        for curr in currency_data:
            Currency.objects.create(country=country, **curr)
        for idd in idd_data:
            suffix_data = idd.pop('suffix', [])
            idd_obj = Idd.objects.create(country=country, **idd)
            for s in suffix_data:
                suffix.objects.create(Idd=idd_obj, **s)
                
        for cap in capital_data:
            capital.objects.create(country=country, **cap)
        
        for alt in alt_spelling_data:
            altSpellings.objects.create(country=country, **alt)
        for lang in language_data:
            Language.objects.create(country=country, **lang)
        for border in border_data:
            Border.objects.create(country=country, **border)
        for dem in demonym_data:
            Demonym.objects.create(country=country, **dem)
        
        for trans in translation_data:
            Translation.objects.create(country=country, **trans)
        for gini in ginis_data:
            Gini.objects.create(country=country, **gini)
        for time in timezone_data:
            Timezone.objects.create(country=country, **time)
        for cont in continent_data:
            Continent.objects.create(country=country, **cont)
        for flag in flags_data:
            Flag.objects.create(country=country, **flag)
        for coat in coat_of_arm_data:
            CoatOfArms.objects.create(country=country, **coat)
        for postal in postal_code_data:
            PostalCode.objects.create(country=country, **postal)
        for cap_info in capital_infos_data:
            capitalInfo.objects.create(country=country, **cap_info)
            
                    
        for car in car_data:
            sign_data = car.pop('sign', [])
            car_obj = Car.objects.create(country=country, **car)
            for sign in sign_data:
                CarSign.objects.create(car=car_obj, **sign) 
                
        

        return country
    
    def update(self, instance, validated_data):
        def upsert_related(model, related_name, data_list):
            related_manager = getattr(instance, related_name)
            # DELETE existing related data first
            related_manager.all().delete()
            # Create new entries
            for item in data_list:
                model.objects.create(country=instance, **item)

        # Pop nested data
        native_name_data = validated_data.pop('native_name', None)
        tld_data = validated_data.pop('tld', None)
        currency_data = validated_data.pop('currency', None)
        idd_data = validated_data.pop('idd', None)
        car_data = validated_data.pop('car', None)
        capital_data = validated_data.pop('capital', None)
        alt_spelling_data = validated_data.pop('alt_spelling', None)
        language_data = validated_data.pop('language', None)
        border_data = validated_data.pop('border', None)
        demonym_data = validated_data.pop('demonym', None)
        translation_data = validated_data.pop('translation', None)
        ginis_data = validated_data.pop('ginis', None)
        timezone_data = validated_data.pop('timezone', None)
        continent_data = validated_data.pop('continent', None)
        flags_data = validated_data.pop('flags', None)
        coat_of_arm_data = validated_data.pop('coat_of_arm', None)
        postal_code_data = validated_data.pop('postal_code', None)
        capital_infos_data = validated_data.pop('capital_infos', None)

        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        
        if native_name_data is not None:
            upsert_related(NativeName, 'native_names', native_name_data)

        if tld_data is not None:
            upsert_related(TopLevelDomain, 'tlds', tld_data)

        if currency_data is not None:
            upsert_related(Currency, 'currencies', currency_data)

        if capital_data is not None:
            upsert_related(capital, 'capitals', capital_data)

        if alt_spelling_data is not None:
            upsert_related(altSpellings, 'alt_spellings', alt_spelling_data)

        if language_data is not None:
            upsert_related(Language, 'languages', language_data)

        if border_data is not None:
            upsert_related(Border, 'borders', border_data)

        if demonym_data is not None:
            upsert_related(Demonym, 'demonyms', demonym_data)

        if translation_data is not None:
            upsert_related(Translation, 'translations', translation_data)

        if ginis_data is not None:
            upsert_related(Gini, 'gini', ginis_data)

        if timezone_data is not None:
            upsert_related(Timezone, 'timezones', timezone_data)

        if continent_data is not None:
            upsert_related(Continent, 'continents', continent_data)

        if flags_data is not None:
            upsert_related(Flag, 'flag', flags_data)

        if coat_of_arm_data is not None:
            upsert_related(CoatOfArms, 'coat_of_arms', coat_of_arm_data)

        if postal_code_data is not None:
            upsert_related(PostalCode, 'postal_codes', postal_code_data)

        if capital_infos_data is not None:
            upsert_related(capitalInfo, 'capital_info', capital_infos_data)

        
        if idd_data is not None:
            instance.idds.all().delete()
            for idd in idd_data:
                suffix_data = idd.pop('suffix', [])
                idd_obj = Idd.objects.create(country=instance, **idd)
                for s in suffix_data:
                    suffix.objects.create(Idd=idd_obj, **s)

        
        if car_data is not None:
            instance.cars.all().delete()
            for car in car_data:
                sign_data = car.pop('sign', [])
                car_obj = Car.objects.create(country=instance, **car)
                for sign in sign_data:
                    CarSign.objects.create(car=car_obj, **sign)

        return instance


      
      
      
        
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
        fields = ['name', 'official','nativeName','tld',
                  'cca2', 'ccn3', 'cioc', 'independent','status','un_member','currency',
                  'idd','capital','altSpellings','region',
                  'subregion','languages','latitude','longitude','landlocked','borders','area',
                  'demonyms','cca3','translations','flag_emoji','google_maps','openstreet_maps','population',
                  'gini','fifa','car','timezones','continents',
                  'flags','coatOfArms','startOfWeek','capitalInfo','postalCode'
                  ]
        

    
class CountryListSerializer(serializers.ModelSerializer):
    capital = serializers.SerializerMethodField()
    timezones = serializers.SerializerMethodField()
    flags = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()
    
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
    
    def get_capital(self, obj):
        capitals = obj.capitals.all()
        if not capitals:
            return []
        return [data.capital for data in capitals]
    
    def get_timezones(self, obj):
        timezones = obj.timezones.all()
        if not timezones:
            return []
        return [data.name for data in timezones]
    
    def get_languages(self, obj):
        languages = obj.languages.all()
        if not languages:
            return []
        result = {}
        for lang in languages:
            result[lang.code] = lang.name
        return result
    
    class Meta:
        model = Country
        fields = ['name', 'official', 'cca2','region','capital', 'population','timezones','flags','languages']       