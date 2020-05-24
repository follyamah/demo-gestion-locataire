from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django.db import transaction, IntegrityError
#from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404 # For displaying in template
#from django.urls import reverse_lazy
from django.utils import timezone
from .models import Utilisateur















"""
def ajouter_chambre(request, ):
    title = "Ajouter Chambre"
    chambre = Chambre.objects.none()
    if request.method == 'POST':
        chambre_form = ChambreForm(request.POST)
        if chambre_form.is_valid():
            try:
                with transaction.atomic():
                    chambre = Chambre(
                        type_chambre=chambre_form.cleaned_data.get('type_chambre'),
                        nom=chambre_form.cleaned_data.get('nom_chambre'),
                        prix=chambre_form.cleaned_data.get('prix'),
                        statut=chambre_form.cleaned_data.get('statut'),
                        maison=chambre_form.cleaned_data.get('maisons'),

                    )
                    chambre.save()


            except IntegrityError:
                raise Http404
            return render(
                request,
                'maison_detail.html', {
                    'chambre': chambre,
                }
            )
    else:
        chambre_form = ChambreForm()

    return render(
        request,
        'ajouter_chambre.html', {
            'title': title,
            'chambre_form': chambre_form,
        }
    )
    """

def reserve_success(request):
    pass
