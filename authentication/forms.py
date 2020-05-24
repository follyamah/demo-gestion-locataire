from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(label='',
        widget=forms.TextInput(
            attrs={
                "placeholder" : "",
                "class": "form-control"
            }
        ))
    password = forms.CharField(label='',
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Mot de passe",
                "class": "form-control"
            }
        ))




class SignUpForm(UserCreationForm):
    '''
    Creer un nouvel Utilisateur
    '''
    username = forms.CharField(max_length=30, required=False, label='Utilisteur',
     widget=forms.TextInput()
)

    email = forms.EmailField(max_length=254, label='Email',
     widget=forms.TextInput()
)
    profile_image = forms.ImageField( required=False,  label='Photo'

)


    password1 = forms.CharField(label="Mot de passe",
                                 strip=False,
                                 widget=forms.PasswordInput()
                                       )



    password2 = forms.CharField(label="Confirmer le mot de passe",
                                 strip=False,
                                 widget=forms.PasswordInput()
                                       )





    CHOICES=[('1','Je suis Locataire'),
         ('2','Je suis Administrateur'),
         ('3','Je suis Gestionnaire du Systeme')]
    role = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), help_text='Pardon Selectionnez un Role:', initial='1')

    class Meta:
        model = Utilisateur
        fields = ('username', 'email', 'password1', 'password2','profile_image')





    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Mot de passe\'different!')
        return cd['password2']
