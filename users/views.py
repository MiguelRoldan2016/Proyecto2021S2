from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
# from django.contrib import messages
from django.contrib.auth import authenticate, login, views as auth_views

from .forms import RegisterForm


class LoginView (auth_views.LoginView):
    template_name = 'login.html'


def registration_view(request):
    context = {}
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('index')
        else:
            context['registration_form'] = form
    else:
        form = RegisterForm()
        context['registration_form'] = form
    return render(request, 'registration/registro.html', context)
