from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, views as auth_views
from django.views.generic.edit import FormView

from . import forms


class LoginView(auth_views.LoginView):
    template_name = 'login.html'


class NewLoginView(FormView):
    """login view"""

    form_class = forms.NewLoginForm
    success_url = reverse_lazy('index')
    template_name = 'login.html'

    def form_valid(self, form):
        """ process user login"""
        credentials = form.cleaned_data

        user = authenticate(username=credentials['email'],
                            password=credentials['password'])

        print('*** //// === POST')
        print(form.fotoData)

        if user is not None:
            print('blablabla1a')
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)

        else:
            print('blablabla1b')
            messages.add_message(self.request, messages.INFO, 'Wrong credentials\
                                please try again')
            return HttpResponseRedirect(reverse_lazy('login'))


def registration_view(request):
    context = {}
    if request.POST:
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            request.session['fotoData'] = form.cleaned_data.get('fotoData')

            user = authenticate(request=request,
                                email=email,
                                password=raw_password)
            login(request, user)
            return redirect('index')
        else:
            context['registration_form'] = form
    else:
        form = forms.RegisterForm()
        context['registration_form'] = form
    return render(request, 'registration/registro.html', context)


def logout_view(request):
    print('logout')
    logout(request)
    return redirect('index')
