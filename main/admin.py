from django.contrib import admin

from .models import Utilisateur


# Register your models here.

@admin.register(Utilisateur)
class Utilisateur(admin.ModelAdmin):
    # To show in admin app
    list_display = (

        'user',
        'prenom_utilisateur',
        'nom_utilisateur',
        'contact_no',
        'address',
        'email_address',
    )
    # Adding search bar
    search_fields = [

        'user',
        'prenom_utilisateur',
        'nom_utilisateur',
        'contact_no',
        'address',
        'email_address',

    ]
    # Categorizing the fields
    fieldsets = (
        (None, {
            'fields': ('profile_picture', ('prenom_utilisateur', 'nom_utilisateur'),)
        }),
        ('Contact Information', {
            'fields': (('contact_no', 'email_address'), 'address')
        }))
