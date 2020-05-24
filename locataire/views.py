
from django.views.generic import (CreateView, DeleteView, ListView, FormView, UpdateView, ListView, DetailView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
#from  .models import  Locataire
from chambre.models import Chambre
#from .forms import LocataireForm, LocataireInfoForm




"""

def list_locataire(request):
    if request.method == 'GET':
        liste_locataires = Locataire.objects.all()
        #liste_maisons = Maison.objects.all()
        context = {
            "locataires": liste_locataires,
            #"liste_maison": liste_maisons,
        }
    return render(request, 'locataire/list_locataire.html', context)



def detail_locataire(request, locataire_id):
    locataire = Locataire.objects.get(pk=locataire_id)
    detail = LocataireInfo.objects.get(pk=locataire_id)

    def age(dob):
        today = date.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    instructorAge = age(details.dateOfBirth)
    qualifications = TeacherQualification.objects.all()

    context = {
        'locataire': locataire,
        'detail': detail,


    }
    return render(request, 'locataire/detail.html', context)




def locataire_view(request):
"""
    #Creer nouveau  locataire
"""
    if request.method == 'POST':
        locataire_form = LocataireForm(request.POST)
        if locataire_form.is_valid():
            locataire_form.save()
            return redirect('locataire:liste-locataire')
    form = LocataireForm()
    context = {
        "form": form
    }
    return render(request, 'locataire/ajouter_locataire.html', context)






def supprimer_locataire(request, pk):
   try:
       locataire = Locataire.objects.get(pk=pk)
       locataire.delete()

   except Locataire.DoesNotExist:
       locataire = None

   return redirect('locataire:liste-locataire')


   def test_func(self):

        if self.request.user.user_type != 3:
            print('Vous n''etes pas autorise ')
            return False

        return True




class Locataire_mise_ajour(LoginRequiredMixin, UpdateView):
    model = Locataire
    fields = '__all__'
    template_name = 'locataire/ajouter_locataire.html'

    def get_success_url(self):

        return reverse_lazy('locataire:liste-locataire')
 """
