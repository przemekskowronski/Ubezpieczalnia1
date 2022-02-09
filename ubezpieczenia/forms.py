from django.forms import ModelForm
from .models import Ocena

class OcenaForm(ModelForm):
    class Meta:
        model = Ocena
        fields = ['recenzja', 'gwiazdki', 'ubezpieczenie']