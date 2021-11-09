import datetime
from django.contrib.auth import authenticate, login
from django.views import generic
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.base import View
from django.views.generic.edit import FormView

from .forms import RenovarPrestamoModelForm, AutorModelForm, NewLoginForm, EjemplarModelForm
from .models import Autor, Ejemplar, Publicacion
from biblioteca.utils import detect_face


class NewLoginView(FormView):
    form_class = NewLoginForm
    template_name = 'newlogin.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        """ process user login"""
        credentials = form.cleaned_data
        self.request.session['fotoData'] = {}

        user = authenticate(request=self.request,
                            username=credentials['email'],
                            password=credentials['password'])

        if user is not None:
            self.request.session['fotoData'] = detect_face(
                form.cleaned_data['fotoData'])
            if self.request.session['fotoData'] is None:
                messages.add_message(self.request, messages.INFO,
                                     'No se detectó ninguna cara. \
                                     Por favor capture una imagen')
                return HttpResponseRedirect(reverse_lazy('newlogin'))

            login(self.request, user)
            return HttpResponseRedirect(self.success_url)

        else:
            messages.add_message(self.request, messages.INFO,
                                 'Credenciales incorrectas. \
                                 Por favor intente de nuevo')
            return HttpResponseRedirect(reverse_lazy('newlogin'))


def index(request):
    # Vista para la pagina inicial del sitio

    cantidad_publicaciones = Publicacion.objects.count()
    cantidad_ejemplares = Ejemplar.objects.count()
    cantidad_ejemplares_disponibles = Ejemplar.objects.filter(
        disponibilidad__exact='d').count()
    cantidad_autores = Autor.objects.count()

    if not request.user.is_authenticated:
        request.session['fotoData'] = {}

    fotoData = request.session.get('fotoData')

    cantidad_visitas = request.session.get('num_visits', 0)
    request.session['num_visits'] = cantidad_visitas+1

    context = {
        'cantidad_publicaciones': cantidad_publicaciones,
        'cantidad_ejemplares': cantidad_ejemplares,
        'cantidad_ejemplares_disponibles': cantidad_ejemplares_disponibles,
        'cantidad_autores': cantidad_autores,
        'cantidad_visitas': cantidad_visitas,
        'fotoData': fotoData,
    }

    return render(request, 'index.html', context=context)


class PublicacionListView(LoginRequiredMixin, generic.ListView):
    model = Publicacion
    paginate_by = 10


class PublicacionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Publicacion
    paginate_by = 10


class AutorListView(LoginRequiredMixin, generic.ListView):
    model = Autor
    paginate_by = 10


class AutorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Autor
    paginate_by = 10


class AutorUpdate(PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'catalogo.puede_crear_autor'
    model = Autor
    form_class = AutorModelForm


class AutorCreate(PermissionRequiredMixin, generic.CreateView):
    permission_required = 'catalogo.puede_crear_autor'
    model = Autor
    form_class = AutorModelForm


class PrestamosPorUsuarioView(LoginRequiredMixin, generic.ListView):
    # Ejemplares prestados al usuario actual
    model = Ejemplar
    template_name = 'catalogo/ejemplares_prestados.html'
    paginate_by = 10

    def get_queryset(self):
        return Ejemplar.objects.filter(prestado_a=self.request.user). \
            filter(disponibilidad='p').order_by('fecha_vencimiento')


class PrestamosView(PermissionRequiredMixin, generic.ListView):
    # Todos los Ejemplares prestados
    permission_required = 'catalogo.puede_ver_prestamos'
    model = Ejemplar
    template_name = 'catalogo/prestamos.html'
    paginate_by = 10

    def get_queryset(self):
        return Ejemplar.objects.filter(disponibilidad='p'). \
            order_by('fecha_vencimiento')


class EjemplarDetailView(LoginRequiredMixin, generic.UpdateView):
    model = Ejemplar
    template_name = 'catalogo/reservar_ejemplar.html'
    form_class = EjemplarModelForm


@login_required
@permission_required('catalogo.puede_marcar_devolucion', raise_exception=True)
def renovar_prestamo(request, pk):
    # Renovar prestamo de un ejemplar
    ejemplar = get_object_or_404(Ejemplar, pk=pk)

    if request.method == 'POST':
        form = RenovarPrestamoModelForm(request.POST)

        if form.is_valid():
            ejemplar.fecha_vencimiento = form.cleaned_data['fecha_vencimiento']
            ejemplar.save()

            return HttpResponseRedirect(reverse('prestamos'))

    else:
        fecha_propuesta = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenovarPrestamoModelForm(
            initial={'fecha_vencimiento': fecha_propuesta})

    context = {
        'form': form,
        'ejemplar': ejemplar
    }

    return render(request, 'catalogo/renovar_prestamo.html', context)
