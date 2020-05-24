from django.urls import path
from .views import  index,List_maison,maison,supprimer_maison, Maison_mise_ajour,detail_maison

app_name ="maison"

urlpatterns = [
path('', index , name='index'),
#path('maison-detail/<slug>/', MaisonDetailView.as_view(), name='maison-detail'),
path('liste-maison/', List_maison.as_view() , name='liste-maison'),
path('ajouter-maison/', maison , name='ajouter-maison'),
path('<int:pk>/delete/', supprimer_maison, name='supprimer-maison'),
path('editMaison/<int:pk>/', Maison_mise_ajour.as_view(), name='editMaison'),
path('maison-detail/<int:pk>/',detail_maison , name='maison-detail'),
]
