from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,
         name='index'),
    path('publicaciones/', views.PublicacionListView.as_view(),
         name='publicaciones'),
    path('publicacion/<int:pk>', views.PublicacionDetailView.as_view(),
         name='publicacion-detail'),
    path('publicacion/<uuid:pk>/reserva/',
         views.EjemplarDetailView.as_view(),
         name='reservar-ejemplar'),
    path('publicacion/<uuid:pk>/renovacion/',
         views.renovar_prestamo,
         name='renovar-prestamo'),
    path('autores/', views.AutorListView.as_view(),
         name='autores'),
    path('autor/crear/', views.AutorCreate.as_view(),
         name='autor-create'),
    path('autor/<int:pk>', views.AutorDetailView.as_view(),
         name='autor-detail'),
    path('autor/<int:pk>/editar/', views.AutorUpdate.as_view(),
         name='autor-update'),
    path('mis-prestamos/', views.PrestamosPorUsuarioView.as_view(),
         name='mis-prestamos'),
    path('prestamos/', views.PrestamosView.as_view(),
         name='prestamos'),
    path('newlogin/', views.NewLoginView.as_view(),
         name='newlogin'),

]
