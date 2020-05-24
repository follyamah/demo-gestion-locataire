from  django import forms
from .models import  *


class MaisonForm(forms.ModelForm):
   class Meta:

      model = Maison
      fields = ('slug', 'nom_maison','total_chambre','quartier')
      labels={
          'slug':'Le numero de la chambre',
          'nom_maison':'Nom de la maison',
          'total_chambre':'Nombre de chambre',
          'quartier':'Ville/Quartier'

      }
