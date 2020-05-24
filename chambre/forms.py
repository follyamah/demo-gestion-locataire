

from  django import forms
from .models import  *
from chambre.models import Chambre

class ChambreForm(forms.ModelForm):
   class Meta:

      model = Chambre
      fields = ('type_chambre', 'nom','prix','statut','maison')
      labels={
          'type_chambre':'Type de chambre',
          'nom':'Nom de la chambre',
          'prix':'Prix',
          'statut':'Statut',
          'maison':'Maison'
      }




class ChambreForm(forms.Form):




            STATUS_CHOICES = (
            ('L', 'Libre'),
            ('O', 'Occupee'),
            ('I', 'Indisponible')


            )


            maison =forms.ModelChoiceField(queryset=Maison.objects.all(), empty_label=None, label='Maison')
            statut = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect(), help_text='Pardon Selectionnez le statut de la chambre:', initial='1')

            nom= forms.CharField(
            label='Nom',
            widget=forms.TextInput(attrs={'placeholder': 'Nom'})

            )
            prix= forms.FloatField(
            label='Prix',
            widget=forms.TextInput(attrs={'placeholder': 'Prix'})
            )

            type_chambre= forms.CharField(
            label="Type de chambre",
            widget=forms.TextInput(attrs={'placeholder': 'Type de chambre'})
            )



            """
            def clean_chambre(self):
                cleaned_data= super(ChambreForm,self).clean()
                chambre = cleaned_data.get('chambre')
                maison =cleaned_data.get('maison')



                if chambre and maison:
                   chambre = [chambre,maison]
                   rep=''.join(chambre)
                return rep
             """
