from django.urls import path
from .views import *

app_name="payement"

urlpatterns = [

    path('ajouter-payement/', payement , name='ajouter-payement'),
    path('liste-payement/', list_payement , name='liste-payement'),
    path('<int:pk>/supprimer-payement/', supprimer_payement, name='supprimer-payement'),
    path('<int:pk>/modifier-payement/', Payement_mise_ajour.as_view(), name='modifier-payement'),
    path('search-annee/', search_annee , name='search-annee'),



    ]
