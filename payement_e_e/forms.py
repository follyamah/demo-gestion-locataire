from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
from maison.models import Maison
from chambre.models import Chambre
from .models import Payement_e_e
from payement.models import Annee, Mois
from contrat.models import Contrat



class PayementForm_e_e(forms.Form):
    chambre =forms.ModelChoiceField(queryset=Chambre.objects.all().filter(statut='O'), empty_label=None, label='Chambre')
    locataire = forms.ModelChoiceField(queryset=Contrat.objects.filter(date_sortie__isnull=True), empty_label=None, label='Locataire')
    annee = forms.ModelChoiceField(queryset=Annee.objects.all(), empty_label=None, label='Annee')
    mois = forms.ModelChoiceField(queryset=Mois.objects.all(), empty_label=None, label='Mois')




    montant_eau= forms.CharField(
          label='Frais d\'eau',
          widget=forms.TextInput()

      )


    montant_el= forms.CharField(
         label='Frais d\'electricite',
         widget=forms.TextInput()

     )

    date_payement= forms.DateTimeField(
           label='Date de payement',
           widget=forms.TextInput()
       )





    def clean_mois_annee(self):
        cleaned_data =super(PayementForm,self).clean()
        mois = cleaned_data.get('mois')
        annee = cleaned_data.get('annee')
        locataire = cleaned_data.get('locataire')

        if mois and annee and locataire:

          if mois.exists() and annee.exists() and locataire.exists():
              raise ValidationError(('Ce payement est deja fait'))


        return cleaned_data


    """
        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
    """
        # Remember to always return the cleaned data.


    """

     def clean_utilisateur(self):
            utilisateur = self.cleaned_data['utilisateur']



            if utilisateur.user_type !=3:
               raise ValidationError(('Vous n''est  pas autorise a signer ce contrat!'))

            return utilisateur
     """
