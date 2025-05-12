from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    official = models.CharField(max_length=200, blank=True, null=True)
    cca2 = models.CharField(max_length=2, unique=True)
    cca3 = models.CharField(max_length=3, blank=True, null=True)
    ccn3 = models.CharField(max_length=3, blank=True, null=True)
    cioc = models.CharField(max_length=3, blank=True, null=True)
    independent = models.BooleanField(default=False , blank=True, null=True)
    status = models.CharField(max_length=50,default='officially-assigned', blank=True, null=True)
    un_member = models.BooleanField(default=False)
    region = models.CharField(max_length=50, blank=True, null=True)
    subregion = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    landlocked = models.BooleanField(default=False , blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    flag_emoji  = models.CharField(max_length=200, blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)
    fifa = models.CharField(max_length=10, blank=True, null=True)
    startOfWeek = models.CharField(max_length=10, blank=True, null=True)
    
    google_maps = models.URLField(blank=True, null=True)
    openstreet_maps = models.URLField(blank=True, null=True)
    
    # Add other fields as needed

    def __str__(self):
        return self.name
    
class capital(models.Model):
    country = models.ForeignKey(Country, related_name='capitals', on_delete=models.CASCADE)
    capital = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.country.name

class Currency(models.Model):
    country = models.ForeignKey(Country, related_name='currencies', on_delete=models.CASCADE)
    code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    symbol = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.country.name
    
class Language(models.Model):
    country = models.ForeignKey(Country, related_name='languages', on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.country.name
    
class Border(models.Model):
    country = models.ForeignKey(Country, related_name='borders', on_delete=models.CASCADE)
    border_country_code = models.CharField(max_length=3)

    def __str__(self):
        return self.country.name
    
class Timezone(models.Model):
    country = models.ForeignKey(Country, related_name='timezones', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.country.name
    
class TopLevelDomain(models.Model):
    country = models.ForeignKey(Country, related_name='tlds', on_delete=models.CASCADE)
    domain = models.CharField(max_length=10)

    def __str__(self):
        return self.country.name
    
class Continent(models.Model):
    country = models.ForeignKey(Country, related_name='continents', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.country.name 
    
class Flag(models.Model):
    country = models.ForeignKey(Country, related_name='flag', on_delete=models.CASCADE)
    png_url = models.URLField(blank=True, null=True)
    svg_url = models.URLField(blank=True, null=True)
    alt_text = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Flag of {self.country.name}"
    
class CoatOfArms(models.Model):
    country = models.ForeignKey(Country, related_name='coat_of_arms', on_delete=models.CASCADE)
    png_url = models.URLField(blank=True, null=True)
    svg_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Coat of Arms of {self.country.name}"

class NativeName(models.Model):
    country = models.ForeignKey(Country, related_name='native_names', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    official = models.CharField(max_length=100, blank=True, null=True)
    common = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.country.name
    
    
class Idd(models.Model):
    country = models.ForeignKey(Country, related_name='idds', on_delete=models.CASCADE)
    root = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.country.name

class suffix(models.Model):
    Idd = models.ForeignKey(Idd, related_name='suffixes', on_delete=models.CASCADE)
    suffix = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.Idd.country.name
    

    
class altSpellings(models.Model):
    country = models.ForeignKey(Country, related_name='alt_spellings', on_delete=models.CASCADE)
    alt_spelling = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.country.name
    

    
class Demonym(models.Model):
    country = models.ForeignKey(Country, related_name='demonyms', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    f = models.CharField(max_length=100, blank=True, null=True)
    m = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.country.name

class Translation(models.Model):
    country = models.ForeignKey(Country, related_name='translations', on_delete=models.CASCADE)
    language = models.CharField(max_length=100, blank=True, null=True)
    official = models.CharField(max_length=100, blank=True, null=True)
    common = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.country.name
    


    
class Gini(models.Model):
    country = models.ForeignKey(Country, related_name='gini', on_delete=models.CASCADE)
    year = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.country.name



class Car(models.Model):
    country = models.ForeignKey(Country, related_name='cars', on_delete=models.CASCADE)
    side = models.CharField(max_length=10, blank=True, null=True)
    def __str__(self):
        return self.country.name

class CarSign(models.Model):
    car = models.ForeignKey(Car, related_name='car_sign', on_delete=models.CASCADE)
    sign = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.car.country.name

    
class capitalInfo(models.Model):
    country = models.ForeignKey(Country, related_name='capital_info', on_delete=models.CASCADE)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.country.name

class PostalCode(models.Model):
    country = models.ForeignKey(Country, related_name='postal_codes', on_delete=models.CASCADE)
    format = models.CharField(max_length=100, blank=True, null=True)
    regex = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.country.name