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
from .forms import PayementForm
from .models import Payement, Mois, Annee
from chambre.models import Chambre
from django.contrib import messages

# Create your views here.







def list_payement(request):
    if request.method == 'GET':
        liste_payements = Payement.objects.all().order_by('locataire','annee','mois')[:12]
        context = {
            "payement": liste_payements,

        }
    return render(request, 'payement/list_payement.html', context)




"""
def contrat(request):
    '''
    creer un contrat
    '''
    if request.method == 'POST':
        form = ContratForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contrat:list-contrat')
    else:
        form = ContratForm()
    total_contrat = Contrat.objects.all()
    ctx = {
        'form': form,
        'contrats': total_contrat,
    }
    return render(request, 'contrat/ajouter_contrat.html', ctx)
    """

def supprimer_payement(request, pk):
   try:
       payement = Payement.objects.get(pk=pk)
       payement.delete()

   except Payement.DoesNotExist:
       payement = None

   return redirect('payement:liste-payement')





def payement(request):
    msg = None
    form = PayementForm()
    if request.method == 'POST':
        form = PayementForm(request.POST)
        if form.is_valid():
            locataire = form.cleaned_data['locataire']
            chambre=form.cleaned_data['chambre']
            mois = form.cleaned_data['mois']
            annee = form.cleaned_data['annee']
            montant = form.cleaned_data['montant']
            date_payement = form.cleaned_data['date_payement']



            payement = Payement.objects.filter(locataire=locataire, mois=mois, annee=annee)


            if payement.exists():

                 msg = 'Ce payement est deja fait'
            else:



                instance = Payement.objects.create(
                    locataire =locataire,
                    chambre=chambre,
                    montant=montant,
                    annee=annee,
                    mois=mois,
                    date_payement=date_payement,



                    )


                return redirect('payement:liste-payement')

    else:
        form = PayementForm()

    context = {
        'form': form,
        'msg':msg,

    }
    return render(request, 'payement/ajouter_payement.html', context)






class Payement_mise_ajour(LoginRequiredMixin, UpdateView):
       model = Payement
       fields = '__all__'
       template_name = 'payement/ajouter_payement.html'

       def get_success_url(self):

           return reverse_lazy('payement:liste-payement')






def search_annee(request):
        query = request.GET.get('query')
        if not query:
            payement = Payement.objects.all()
        else:
            # title contains the query is and query is not sensitive to case.

            payement =Payement.objects.all().filter(annee__annee=query)

        context = {
            'payement': payement,

        }
        return render(request, 'contrat/detail.html', context)
