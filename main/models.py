from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse





class Utilisateur(models.Model):
    """ Model for staffs """
    profile_picture = models.ImageField(upload_to='utilisateur_img/', default='images/staff.png')
    prenom_utilisateur = models.CharField(max_length=50)
    nom_utilisateur = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=15)
    address = models.CharField(max_length=100 , blank=True)
    email_address = models.EmailField( null = True, blank =True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, editable=False)

    class Meta:
        ordering = ['prenom_utilisateur',  'nom_utilisateur']
        permissions = (("peut voir les utilisteurs",  'Peut voir les utilisteurs'), ('Peut voir le detail  des utilisteurs', 'Peut voir le detail  des utilistaurs'))

    def __str__(self):  # Unicode support
        return '({0}) {1} {2}'.format(self.pk, self.prenom_utilisateur, self.nom_utilisateur)
