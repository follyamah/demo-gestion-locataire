from django.db import models
from maison.models import Maison




STATUS_CHOICES = (
    ('L', 'Libre'),
    ('O', 'Occupee'),
    ('I', 'Indisponible')


)

class Chambre(models.Model):
     type_chambre = models.CharField(max_length=50, null=True, blank=True)
     maison = models.ForeignKey(Maison, on_delete=models.CASCADE, editable=True)
     nom = models.CharField(max_length=25)
     prix = models.FloatField()
     statut = models.CharField(choices=STATUS_CHOICES, max_length=1)




     class Meta:
        ordering = ['nom' ]
        permissions = (('peut voir chamnbre', 'Peut voir chambre'),('peut voir detail chamnbre', 'Peut voir  detail chambre'))

     def get_absolute_url(self):
        return reverse('chambre-detail', args=str([self.pk]))

     def __str__(self):
        return   '{0}'.format( self.nom)

     def is_statut(self):
         if self.statut =='L':
             return True
         return False
