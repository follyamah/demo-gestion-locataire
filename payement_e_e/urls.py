from django.urls import path
from .views import *

app_name="payement_e_e"

urlpatterns = [

    path('ajouter-payement_e_e/', payement_e_e , name='ajouter-payement_e_e'),
    path('liste-payement_e_e/', list_payement_e_e , name='liste-payement_e_e'),
    path('<int:pk>/supprimer-payement_e_e/', supprimer_payement_e_e, name='supprimer-payement_e_e'),
    path('<int:pk>/modifier-payement_e_e/', Payement_mise_ajour.as_view(), name='modifier-payement_e_e'),
    path('search-annee_e_e/', search_annee_e_e , name='search-annee_e_e'),



    ]
