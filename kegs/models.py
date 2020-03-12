from django.db import models
from django.urls import reverse

# Create your models here.
class Beer(models.Model):
    name = models.TextField(max_length=50)
    style = models.TextField(max_length=30)
    abv = models.DecimalField(max_digits=3, decimal_places=1)
    bitterness = models.IntegerField()
    datebrewed = models.DateField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('kegs:beer_edit', kwargs={'pk':self.pk})

class Keg(models.Model):
    number = models.IntegerField()
    beer = models.ForeignKey('Beer', on_delete=models.SET_NULL, null=True)
    status = models.TextField(max_length=15)
    dateupdated = models.DateField()

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('kegs:keg_edit', kwargs={'pk':self.pk})