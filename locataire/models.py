from django.db import models






"""
SEXE_CHOICES = (
    ('F', 'Feminin'),
    ('M', 'Masculin')

)


class Locataire(models.Model):
    #Model Locataire
    nom_locataire = models.CharField(max_length=50 , null=False, blank=True, unique=True)
    prenom_locataire= models.CharField(max_length=50)
    sexe=models.CharField(choices=SEXE_CHOICES, max_length=1)
    contact_no = models.CharField(max_length=15 , null = True ,blank=True)
    address = models.CharField(max_length=100, null= True, blank=True )
    email_address = models.EmailField(null=True, blank=True)
    """
"""
    class Meta:
        ordering = [ 'nom_locataire','prenom_locataire' ]
        permissions = (('peut voir les locataires', 'Peut voir les locataires'),)

    def get_absolute_url(self):


        This generates the url for customer detail.
        'customer-detail' is the name of the url.
        Takes argument customer_id

        return reverse('locataire-detail', args=str([selfpk]))



    def __str__(self):
        return '{0} {1} '.format( self.nom_locataire, self.prenom_locataire)

    """
