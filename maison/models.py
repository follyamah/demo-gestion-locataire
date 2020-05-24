from django.db import models

# Create your models here.

class Maison(models.Model):
    slug = models.SlugField()
    nom_maison = models.CharField(max_length=150, null=False, blank=True, unique=True)
    total_chambre=models.IntegerField()
    quartier = models.CharField(max_length=50, null=False, blank =True)


    class Meta:
        ordering = [ 'nom_maison']
        permissions = (('peut voir les maisons', 'Peut voir les maisons'),)

    def get_absolute_url(self):

       #This generates the url for customer detail.
       #'customer-detail' is the name of the url.
       #Takes argument customer_id
       return reverse("maison-detail", kwargs={
           'slug': self.slug
       })



    def __str__(self):
        return '{0}'.format(self.nom_maison)
