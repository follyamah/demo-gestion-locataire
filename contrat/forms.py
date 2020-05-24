from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
from .models import Contrat, LocataireInfo
from maison.models import Maison
from chambre.models import Chambre



class ContratForm(forms.Form):
     maison =forms.ModelChoiceField(queryset=Maison.objects.all(), empty_label=None, label='Maison')
     chambre =forms.ModelChoiceField(queryset=Chambre.objects.all().filter(statut='L'), empty_label=None, label='Chambre')


     SEXE_CHOICES = (
      ('M', 'Masculin'),
      ('F', 'Feminin'),


     )

     nom_locataire= forms.CharField(
          label='Nom',
          widget=forms.TextInput()

      )
     prenom_locataire= forms.CharField(
           label='Prenom',
           widget=forms.TextInput()
       )

     sexe = forms.ChoiceField(choices=SEXE_CHOICES, widget=forms.RadioSelect(), help_text='Pardon Selectionnez le sexe:', initial='1')


     contact_no= forms.CharField(
              label='Contact',
              widget=forms.TextInput()
          )


     caution= forms.FloatField(
           label='Caution',
           widget=forms.TextInput()

       )


     address= forms.CharField(
          label='Adresse',
          widget=forms.TextInput()

      )
     email_address= forms.EmailField(
           label='Email',
           widget=forms.TextInput()
       )


     date_contrat= forms.DateTimeField(
          label='Date',
          widget=forms.TextInput()

      )


     date_entree= forms.DateTimeField(
            label='Date d''arrivee',
            widget=forms.TextInput()
        )

     date_sortie= forms.DateTimeField(
              label='Date de depart',
              widget=forms.TextInput(),
              required=False
          )

     profile_image = forms.ImageField(

        label='Photo',
        required=False
      )





     def clean_caution(self):
        chambre = self.cleaned_data['chambre']
        caution =self.cleaned_data['caution']
        if caution != chambre.prix*6:
            raise ValidationError(('Entrez une somme correcte!'))
        return caution


     def clean_email(self):
           email = self.cleaned_data['email_address'].lower()
           r = Contrat.objects.filter(email_address=email)
           if r.count:
               raise ValidationError("{0} existe deja".format(email))
           return email.lower()


     def clean_contact(self):
           contact = self.cleaned_data['contact_no']
           if contact == 'ayite':
              raise ValidationError("{0} est invalide".format(contact))
           return contact



     def clean_chambre_maison(self):
           cleaned_data =super(ContratForm,self).clean()
           chambre = cleaned_data.get('chambre')
           maison = cleaned_data.get('maison')


           if chambre and maison :

             if m.exists() and annee.exists() and locataire.exists():
                 raise ValidationError(('Ce payement est deja fait'))


           return cleaned_data







class LocataireInfoForm(forms.ModelForm):
         class Meta:

            model = LocataireInfo
            fields = ('locataire', 'information')
            labels={
                'locataire':'Locataire ',
                'information':'Information'



            }










"""
        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
"""
        # Remember to always return the cleaned data.

"""
     def clean_contrat(self):
            cleaned_data = super(ContratForm,self).clean()
            maison=cleaned_data.get('maison')
            chambre=cleaned_data.get('chambre')
            if maison is not chambre.maison:
                   raise ValidationError(('Vous n''est  pas autorise a signer ce contrat!'))





            if utilisateur.user_type !=3:
               raise ValidationError(('Vous n''est  pas autorise a signer ce contrat!'))

            return utilisateur
"""
