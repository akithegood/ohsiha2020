from django.forms import ModelForm
from kegs.models import Beer, Keg

class BeerForm(ModelForm):
    class Meta:
        model = Beer
        fields = ['name', 'style', 'abv', 'bitterness', 'datebrewed', 'description']
    
class KegForm(ModelForm):
    class Meta:
        model = Keg
        fields = ['number', 'beer', 'status', 'dateupdated']