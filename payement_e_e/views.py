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
from .forms import PayementForm_e_e
from .models import Payement_e_e, Mois, Annee
from chambre.models import Chambre
from django.contrib import messages

# Create your views here.







def list_payement_e_e(request):
    if request.method == 'GET':
        liste_payements = Payement_e_e.objects.all().order_by('locataire','annee','mois')[:12]
        context = {
            "payement": liste_payements,

        }
    return render(request, 'payement_e_e/list_payement_e.html', context)




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

def supprimer_payement_e_e(request, pk):
   try:
       payement = Payement_e_e.objects.get(pk=pk)
       payement.delete()

   except Payement_e_e.DoesNotExist:
       payement = None

   return redirect('payement_e_e:liste-payement_e_e')





def payement_e_e(request):
    msg = None
    form = PayementForm_e_e()
    if request.method == 'POST':
        form = PayementForm_e_e(request.POST)
        if form.is_valid():
            locataire = form.cleaned_data['locataire']
            chambre=form.cleaned_data['chambre']
            mois = form.cleaned_data['mois']
            annee = form.cleaned_data['annee']
            montant_eau = form.cleaned_data['montant_eau']
            montant_el = form.cleaned_data['montant_el']
            date_payement = form.cleaned_data['date_payement']



            payement = Payement_e_e.objects.filter(locataire=locataire, mois=mois, annee=annee)


            if payement.exists():

                 msg = 'Ce payement est deja fait'
            else:



                instance = Payement_e_e.objects.create(
                    locataire =locataire,
                    chambre=chambre,
                    montant_eau=montant_eau,
                    montant_el=montant_el,
                    annee=annee,
                    mois=mois,
                    date_payement=date_payement,



                    )


                return redirect('payement_e_e:liste-payement_e_e')

    else:
        form = PayementForm_e_e()

    context = {
        'form': form,
        'msg':msg,

    }
    return render(request, 'payement_e_e/ajouter_payement_e.html', context)






class Payement_mise_ajour(LoginRequiredMixin, UpdateView):
       model = Payement_e_e
       fields = '__all__'
       template_name = 'payement_e_e/ajouter_payement_e.html'

       def get_success_url(self):

           return reverse_lazy('payement_e_e:liste-payement_e_e')






def search_annee_e_e(request):
        query = request.GET.get('query')
        if not query:
            payement = Payement_e_e.objects.all()
        else:
            # title contains the query is and query is not sensitive to case.

            payement =Payement_e_e.objects.all().filter(annee__annee=query)

        context = {
            'payement': payement,

        }
        return render(request, 'contrat/detail.html', context)
