from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import (CreateView, DeleteView, ListView, FormView, UpdateView, ListView, DetailView)
from .forms import (SignUpForm, LoginForm)
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Utilisateur












def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if  user.user_type != 3:
                    return redirect("contrat:liste-contrat")
                else:
                    return redirect("/index")


            else:
                msg = 'Invalide'
        else:
            msg = 'Validation echouee'

    return render(request, "registration/login.html", {"form": form, "msg" : msg})



class SignUp(CreateView):
    '''
    Nouvel Utilisateur
    '''
    form_class = SignUpForm
    success_url = reverse_lazy('authentication:login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        role = form.cleaned_data['role']
        profile_image=form.cleaned_data['profile_image']
        obj.user_type = role
        obj.profile_image=profile_image
        form.save()
        return super().form_valid(form)

def logout (request):
    try:
        del request.session[User.id]
    except KeyError:
        pass
    return HttpResponse("Vous etes deconnectes.")
