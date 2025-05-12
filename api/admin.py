from django.contrib import admin
from django.utils.text import slugify
from .models import *


admin.site.register(Country)
admin.site.register(capital)
admin.site.register(Currency)
admin.site.register(Language)
admin.site.register(Border)
admin.site.register(Timezone)
admin.site.register(TopLevelDomain)
admin.site.register(Continent)
admin.site.register(Flag)
admin.site.register(CoatOfArms)
admin.site.register(NativeName)

admin.site.register(Idd)
admin.site.register(suffix)
admin.site.register(altSpellings)
admin.site.register(Demonym)

admin.site.register(Translation)

admin.site.register(Gini)
 
admin.site.register(Car)  
admin.site.register(CarSign)  
admin.site.register(capitalInfo)  
admin.site.register(PostalCode)  