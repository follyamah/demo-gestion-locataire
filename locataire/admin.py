from django.contrib import admin
#from .models import Locataire
# Register your models here.
"""
@admin.register(Locataire)
class LocataireAdmin(admin.ModelAdmin):
    list_display = (

        'prenom_locataire',
        'nom_locataire',
        'sexe',
        'contact_no',
        'address',
        'email_address',
    )
    search_fields = [


        'prenom_locataire',
        'nom_locataire',
        'sexe',
        'contact_no',
        'address',
        'email_address',

    ]

    fieldsets = (
        (None, {
            'fields': (('prenom_locataire', 'nom_locataire','sexe'),)
        }),
        ('Contact Information', {
            'fields': (('contact_no', 'email_address'), 'address'),
        }),)
"""
