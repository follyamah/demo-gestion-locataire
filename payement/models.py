from django.db import models
from contrat.models import Contrat
from chambre.models import Chambre
from django.utils import timezone

# Create your models here.




class Annee(models.Model):
    annee=models.CharField(max_length=50, blank=False)
    def __str__(self):

        return f"{self.annee} "



class Mois(models.Model):
   mois=models.CharField(max_length=30, blank=False)
   def __str__(self):

       return f"{self.mois} "


class Payement(models.Model):
    locataire = models.ForeignKey(Contrat, on_delete=models.CASCADE)
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    annee = models.ForeignKey(Annee, on_delete=models.CASCADE ,blank=False)
    mois = models.ForeignKey(Mois, on_delete=models.CASCADE,blank=False)
    montant = models.FloatField()
    date_payement = models.DateTimeField(default=timezone.now)


    class Meta:

        ordering = ['locataire','annee', 'mois']
        permissions = (('peut voir  payement', 'Peut voir payement'),
                       ('peut voir detail des payements', 'Peut voir detail des payements'),)

    def get_absolute_url(self):
        return reverse('payement-detail',  kwargs={
            'slug': self.pk
        })


    def __str__(self):
        return '{0}'.format(self.mois)
        #return f"{self.pk} of {self.mois }"



    def get_annee(self):
       qs=Payement.objects.filter(id=self.id)
       if  qs.exists():
           return  qs
       else:
           pass
