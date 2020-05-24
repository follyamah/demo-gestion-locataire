from django.urls import path
from .views import *

app_name="contrat"

urlpatterns = [

    path('ajouter-contrat/', contrat , name='ajouter-contrat'),
    path('liste-contrat/', list_contrat , name='liste-contrat'),
    path('<int:pk>/supprimer-contrat/', supprimer_contrat, name='supprimer-contrat'),
    path('<int:pk>/modifier-contrat/', Contrat_mise_ajour.as_view(), name='modifier-contrat'),
    path('locataire-info/', ajouter_locataire_info , name='locataire-info'),
    path('locataire-detail/<int:locataire_id>/',detail_locataire , name='locataire-detail'),
    path('<int:pk>/delete-info/', supprimer_info, name='supprimer-info'),
    path('editinfo/<int:pk>/', Info_mise_ajour.as_view(), name='editinfo'),
    path('search-locataire/', search_maison , name='search-locataire'),




    ]
