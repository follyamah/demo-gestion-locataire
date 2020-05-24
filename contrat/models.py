from django.db import models
from maison.models import Maison
from chambre.models import Chambre
from django.utils import timezone








SEXE_CHOICES = (
    ('M', 'Masculin'),
    ('F', 'Feminin'),


)


class Contrat(models.Model):
    """Models de Contrat"""
    nom_locataire = models.CharField(max_length=50 , null=False, blank=True)
    prenom_locataire= models.CharField(max_length=50)
    sexe=models.CharField(choices=SEXE_CHOICES, max_length=1)
    contact_no = models.CharField(max_length=15 , null = True ,blank=True)
    address = models.CharField(max_length=100, null= True, blank=True )
    email_address = models.EmailField(null=True, blank=True)
    maison =models.ForeignKey(Maison, on_delete=models.CASCADE)
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    caution = models.FloatField()
    date_contrat = models.DateTimeField(default=timezone.now)
    date_entree = models.DateTimeField(default=timezone.now,null=True, blank=True)
    date_sortie = models.DateTimeField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='utilisateur_img/', null=True, blank=True)

    class Meta:
        permissions = (('peut voir  contrat', 'Peut voir contrat'),
                       ('peut voir detail des contrats', 'Peut voir detail des contrats'),)

    def get_absolute_url(self):
        return reverse('contrat-detail', args=str([self.pk]))

    def __str__(self):

        return '{0} {1}'.format(self.nom_locataire, self.prenom_locataire)

    def save(self, *args, **kwargs):  # Overriding default behaviour of save
     if self.chambre:
        self.chambre.statut = ""
     super(Contrat,self).save(*args, **kwargs)


    def is_overdue(self):
        if self.caution   is not self.chambre.prix *12 :
            return True
        return False

    def set_chambre_nom(self,chambre):
         if self.chambre:
              chambre =''.join(self.chambre, self.maison[:5])
              self.chambre=chambre






class LocataireInfo(models.Model):
        locataire = models.OneToOneField(Contrat, on_delete=models.CASCADE)
        information = models.TextField(max_length=400,null=False, blank=False)


        def __str__(self):

            return '{0} '.format( self.information)
