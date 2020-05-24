from django.urls import path
from .views import  (chambre ,liste_chambre, supprimer_chambre, Chambre_mise_ajour,search)

app_name="chambre"

urlpatterns = [

    path('ajouter-chambre/', chambre , name='ajouter-chambre'),
    path('liste-chambre/', liste_chambre , name='liste-chambre'),
    path('<int:pk>/delete_chambre/', supprimer_chambre, name='supprimer-chambre'),
    path('editchambre/<int:pk>/', Chambre_mise_ajour.as_view(), name='editchambre'),
    path('search/', search , name='search'),



    ]
