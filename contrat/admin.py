from django.contrib import admin
from .models import Contrat, LocataireInfo


# Register your models here.


class ContratInstanceInline(admin.TabularInline):
    model = Contrat

class ContratAdmin(admin.ModelAdmin):
    list_display = ( 'nom_locataire','prenom_locataire','sexe','contact_no','address','email_address','maison','chambre','caution','profile_image' )
    list_filter = ('date_contrat', 'date_entree', 'date_sortie')

admin.site.register(Contrat, ContratAdmin)
admin.site.register(LocataireInfo)
