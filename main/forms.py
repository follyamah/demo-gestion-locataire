











#from django import forms
#from .models import Maison
"""
STATUS_CHOICES = (
    ('L', 'libre'),
    ('O', 'occupee'),
    ('I', 'indisponible')


)



class ChambreForm(forms.Form):
"""
   # This is the  form for chambre.
"""
    error_messages = {
        'chambre existant': 'Cette chambre existe deja',
    }
    type_chambre = forms.CharField(
        label=('type_chambre'),
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('Entrez le type de chambre'),
            }
        )
    )
    nom_chambre = forms.CharField(
        label=('nom_chambre'),
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('Entrer le nom de la chambre'),
            }
        )
    )
    prix  =forms.FloatField(
        label=('prix'),
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('Entrer le prix'),
            }
        )
    )

    statut= forms.ChoiceField(
        label=('statut'),
        widget=forms.Select,
        choices=STATUS_CHOICES)

    maisons = forms.ModelChoiceField(queryset=Maison.objects.all(),
        label=('maison'),


    )
    """

"""
    rooms = forms.ModelMultipleChoiceField(
        queryset=Room.objects.filter(reservation__isnull=True),
        widget=FilteredSelectMultiple(
            is_stacked=True,
            verbose_name="Rooms",
            attrs={
                'class': 'form-control',
            },
        ),
    )
"""
