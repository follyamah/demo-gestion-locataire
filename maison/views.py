from django.views.generic import (CreateView, DeleteView, ListView, FormView, UpdateView, ListView, DetailView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from .models import Maison
from  contrat.models import  Contrat
from chambre.models import Chambre
from contrat.models import Contrat
from .forms import MaisonForm
from django.shortcuts import  get_object_or_404

# Create your views here.



def index(request):

    maisons = Maison.objects.all().count()
    chambres = Chambre.objects.all().count()
    contrats = Contrat.objects.all().count()



    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits+1
    """
    current_semester = Semester.objects.get(is_current_semester=True)
    no_of_1st_class_students = Result.objects.filter(cgpa__gte=4.5).count()
    no_of_carry_over_students = CarryOverStudent.objects.all().count()
    no_of_students_to_repeat = RepeatingStudent.objects.all().count()
    """
    context = {
        "maisons": maisons,
        "chambres":chambres,
        "contrats":contrats,
        "num_visits":num_visits,

    }

    return render(request, 'maison/index.html', context)



class  List_maison(ListView):
    model = Maison
    template_name = "maison/list_maison.html"



#@login_required
def maison(request):
    """
    Creer nouvelle  maaison
    """
    if request.method == 'POST':
        maison_form = MaisonForm(request.POST)
        if maison_form.is_valid():
            maison_form.save()
            return redirect('maison:liste-maison')
    form = MaisonForm()
    context = {
        "form": form
    }
    return render(request, 'maison/ajouter_maison.html', context)




def supprimer_maison(request, pk):
   try:
       maison = Maison.objects.get(pk=pk)
       maison.delete()

   except Maison.DoesNotExist:
       maison = None

   return redirect('maison:liste-maison')


   def test_func(self):

        if self.request.user.user_type != 3:
            print('Vous n''etes pas autorise ')
            return False

        return True




class Maison_mise_ajour(LoginRequiredMixin, UpdateView):
    model = Maison
    fields = '__all__'
    template_name = 'maison/ajouter_maison.html'

    def get_success_url(self):

        return reverse_lazy('maison:liste-maison')









def detail_maison(request, pk):
        maison =Chambre.objects.filter(maison__id=pk)


        context = {
            'liste_chambre': maison


        }
        return render(request, 'chambre/list_chambre.html', context)











"""
class Maison_mise_ajour(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''
    Mise a jour Maison
    '''
    model = Maison
    form_class = MaisonForm
    success_url = reverse_lazy('list_maison')
    template_name = 'maison/ajouter_maison.html'
    raise_exception = True

    def test_func(self):
        print(' Utilisateur:{0}'.format(self.request.user.user_type))
        if self.request.user.user_type != 2:
            print('Type d''utilisateur refuse, modification non autorisee')
            return False
        return True

    def get_login_url(self):
        if not self.request.user.is_authenticated:
            print('Veuillez vous authentifier')
            return super(Maison_mise_ajour, self).get_login_url()
        return ''

    def get_context_data(self, **kwargs):
        context = super(Maison_mise_ajour, self).get_context_data(**kwargs)
        context['title'] = "Modification de Maison"
        return context


"""




"""
class MaisonView(ListView):
    model = Maison
    template_name = "index.html"



class MaisonDetailView(DetailView):
    model = Maison
    template_name = "maison_detail.html"
"""
