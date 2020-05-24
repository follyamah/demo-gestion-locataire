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
from .forms import ContratForm, LocataireInfoForm
from .models import Contrat, LocataireInfo
from payement.models import Annee
from chambre.models import Chambre
from payement.models import Payement
from payement_e_e.models import Payement_e_e
from maison.models import Maison

# Create your views here.



def list_contrat(request):
    if request.method == 'GET':
        liste_contrats = Contrat.objects.all()
        liste_maisons = Maison.objects.all()
        context = {
            "contrat": liste_contrats,
            "maison":liste_maisons

        }
    return render(request, 'contrat/list_locataire.html', context)




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

def supprimer_contrat(request, pk):
   try:
       contrat = Contrat.objects.get(pk=pk)
       contrat.delete()

   except Contrat.DoesNotExist:
       contrat = None

   return redirect('contrat:liste-contrat')


def contrat(request):
    msg = None

    form = ContratForm()
    if request.method == 'POST':
        form = ContratForm(request.POST)
        if form.is_valid():
            nom_locataire = form.cleaned_data['nom_locataire']
            prenom_locataire = form.cleaned_data['prenom_locataire']
            sexe = form.cleaned_data['sexe']
            contact_no = form.cleaned_data['contact_no']
            address = form.cleaned_data['address']
            email_address = form.cleaned_data['email_address']
            maison = form.cleaned_data['maison']
            chambre = form.cleaned_data['chambre']
            caution = form.cleaned_data['caution']
            date_contrat = form.cleaned_data['date_contrat']
            date_entree = form.cleaned_data['date_entree']
            date_sortie = form.cleaned_data['date_sortie']
            profile_image=form.cleaned_data['profile_image']

            chambre = Chambre.objects.filter(nom=chambre, maison=maison)
            if chambre is not exists():
                 msg = 'Cette chambre ne se trouve pas dans cette maison'
            else:



                instance = Contrat(
                    nom_locataire=nom_locataire,
                    prenom_locataire=prenom_locataire,
                    sexe=sexe,
                    contact_no=contact_no,
                    address=address,
                    email_address=email_address,
                    maison =maison,
                    chambre=chambre,
                    caution=caution,
                    date_contrat=date_contrat,
                    date_entree=date_entree,
                    date_sortie=date_sortie,
                    profile_image=profile_image,
                    )
                instance.save()
                chambre.statut='O'
                chambre.save()

                return redirect('contrat:liste-contrat')

    else:
        form = ContratForm()

    context = {
        'form': form,
        'msg':msg,

    }
    return render(request, 'contrat/ajouter_contrat.html', context)


class Contrat_mise_ajour(LoginRequiredMixin, UpdateView):
       model = Contrat
       fields = '__all__'
       template_name = 'contrat/ajouter_contrat.html'

       def get_success_url(self):

           return reverse_lazy('contrat:liste-contrat')





def ajouter_locataire_info(request):
    """
      locataire info
    """
    if request.method == 'POST':
        form = LocataireInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contrat:liste-contrat')
    form = LocataireInfoForm()
    context = {
        "form": form
    }
    return render(request, 'contrat/locataire_info.html', context)



def detail_locataire(request, locataire_id):
        locataire = Contrat.objects.filter(id=locataire_id)
        detail =LocataireInfo.objects.filter(locataire__id=locataire_id)
        payement = Payement.objects.filter( locataire__id=locataire_id)[:12]
        payement_e = Payement_e_e.objects.filter( locataire__id=locataire_id)[:12]
        annee=Annee.objects.all()




        """
        def age(dob):
            today = date.today()
            return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        instructorAge = age(details.dateOfBirth)
        qualifications = TeacherQualification.objects.all()
        """

        context = {
            'locataire': locataire,
            'detail': detail,
             'payement':payement,
             'annee':annee,
             'payement_e':payement_e,


        }
        return render(request, 'contrat/detail.html', context)






def supprimer_info(request, pk):
   try:
       info = LocataireInfo.objects.get(pk=pk)
       info.delete()

   except LocataireInfo.DoesNotExist:
       info = None

   return redirect('contrat:liste-contrat')





class Info_mise_ajour(LoginRequiredMixin, UpdateView):
    model = LocataireInfo
    fields = '__all__'
    template_name = 'contrat/locataire_info.html'

    def get_success_url(self):

        return reverse_lazy('contrat:liste-contrat')






def search_maison(request):
        query = request.GET.get('query')
        if not query:
            contrat = Contrat.objects.all()
        else:
            # title contains the query is and query is not sensitive to case.

            contrat =Contrat.objects.all().filter(maison__nom_maison__icontains=query)

        context = {
            'contrat': contrat,

        }
        return render(request, 'contrat/list_locataire.html', context)
