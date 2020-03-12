from django.contrib import admin
from django.db import models

# Register your models here.
from kegs.models import Beer, Keg

class MyBeerAdmin(admin.ModelAdmin):
    model = Beer
    list_display = ('name', 'style', 'abv', 'bitterness', 'datebrewed', 'description',)

class MyKegAdmin(admin.ModelAdmin):
    model = Keg
    list_display = ('number', 'beer', 'status', 'dateupdated',)

admin.site.register(Beer, MyBeerAdmin)
admin.site.register(Keg, MyKegAdmin)