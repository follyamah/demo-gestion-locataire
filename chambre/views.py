from django.views.generic import (CreateView, DeleteView, ListView, FormView, UpdateView, ListView, DetailView)
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.db import transaction, IntegrityError
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView #Signup, ReservationForm, CheckInRequestForm
from .forms import ChambreForm
from .models import Chambre, Maison
# Create your views here.

#@login_required

def liste_chambre(request):
    if request.method == 'GET':
        liste_chambres = Chambre.objects.all()
        liste_maisons = Maison.objects.all()
        context = {
            "liste_chambre": liste_chambres,
            "liste_maison": liste_maisons,
        }
    return render(request, 'chambre/list_chambre.html', context)


def chambre(request):

    msg=None
    form = ChambreForm()
    if request.method == 'POST':
        form = ChambreForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            type_chambre = form.cleaned_data['type_chambre']
            maison = form.cleaned_data['maison']
            statut = form.cleaned_data['statut']
            prix = form.cleaned_data['prix']


            qs=Chambre.objects.filter(maison=maison,nom=nom )
            if qs.exists():
                msg='Cette chambre existe deja dans cette maison'
            else:


                instance = Chambre(
                    nom =nom,
                    type_chambre=type_chambre,
                    maison=maison,
                    statut=statut,
                    prix=prix,

                    )
                instance.save()

                return redirect('chambre:liste-chambre')

    else:
        form = ChambreForm()

    context = {
        'form': form,
        'msg':msg,

    }
    return render(request, 'chambre/ajouter_chambre.html', context)



def supprimer_chambre(request, pk):
   try:
       chambre = Chambre.objects.get(pk=pk)
       chambre.delete()

   except Chambre.DoesNotExist:
       chambre = None

   return redirect('chambre:liste-chambre')





class Chambre_mise_ajour(LoginRequiredMixin, UpdateView):
    model = Chambre
    fields = '__all__'
    template_name = 'chambre/ajouter_chambre.html'

    def get_success_url(self):

        return reverse_lazy('chambre:liste-chambre')





def search(request):
        query = request.GET.get('query')
        if not query:
            chambre = Chambre.objects.all()
        else:
            # title contains the query is and query is not sensitive to case.

            chambre =Chambre.objects.all().filter(maison__nom_maison__icontains=query)

        context = {
            'liste_chambre': chambre,

        }
        return render(request, 'chambre/list_chambre.html', context)
