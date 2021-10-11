from django.db.models.deletion import SET_NULL
from django.conf import settings
from django.urls import reverse
from django.db import models
from datetime import date
import uuid

from simple_history.models import HistoricalRecords
from django.contrib.auth import get_user_model

User = get_user_model()


class IPAddressHistoricalModel(models.Model):
    """
    Abstract model for history models tracking the IP address.
    """
    ip_address = models.GenericIPAddressField(('IP address'))

    class Meta:
        abstract = True


class Genero(models.Model):
    # Modelo que representa un genero literario
    nombre = models.CharField(max_length=200,
                              help_text='Ingrese un genero literario (ej: Narrativa, Ensayo)')
    history = HistoricalRecords(
        bases=[IPAddressHistoricalModel, ]
    )

    class Meta:
        verbose_name = ("Genero")
        verbose_name_plural = ("Generos")

    def __str__(self):
        return self.nombre


class Tipo(models.Model):
    # Modelo que representa el tipo de publicacion
    nombre = models.CharField(max_length=200,
                              help_text='Ingrese un tipo de publicacion (ej: Libro, Revista)')
    history = HistoricalRecords(bases=[IPAddressHistoricalModel, ])

    class Meta:
        verbose_name = ("Tipo")
        verbose_name_plural = ("Tipos")

    def __str__(self):
        return self.nombre


class Idioma(models.Model):
    # Modelo que representa el idioma de la publicacion
    nombre = models.CharField(max_length=200,
                              help_text='Ingrese el idioma de la publicacion (ej: Espanol, Frances)')
    history = HistoricalRecords(bases=[IPAddressHistoricalModel, ])

    class Meta:
        verbose_name = ("Idioma")
        verbose_name_plural = ("Idiomas")

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    # Modelo que representa un autor
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    fecha_muerte = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to=settings.PUBLICACIONES_PICS,
                               default=settings.STATIC_URL+'default.png')
    history = HistoricalRecords(bases=[IPAddressHistoricalModel, ])

    class Meta:
        verbose_name = ("Autor")
        verbose_name_plural = ("Autores")
        ordering = ['apellidos', 'nombres']

    def __str__(self):
        return f'{self.apellidos}, {self.nombres}'

    def get_absolute_url(self):
        return reverse("autor-detail", args=[str(self.id)])


class Publicacion(models.Model):
    # Modelo que representa una publicacion
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(max_length=1000,
                                   help_text='Ingrese una descripcion corta de la publicacion')
    isbn = models.CharField(("ISBN"),
                            max_length=20, unique=True,
                            help_text='Numero de ISBN')
    genero = models.ManyToManyField(
        Genero, help_text='Elija un genero literario')
    idioma = models.ForeignKey(Idioma, on_delete=models.SET_NULL, null=True)
    tipo = models.ManyToManyField(Tipo,
                                  help_text='Elija el tipo de publicacion')
    imagen = models.ImageField(upload_to=settings.PUBLICACIONES_PICS,
                               default=settings.STATIC_URL+'default.png')
    history = HistoricalRecords(bases=[IPAddressHistoricalModel, ])

    class Meta:
        verbose_name = ("Publicacion")
        verbose_name_plural = ("Publicaciones")

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("publicacion-detail", args=[str(self.id)])

    def mostrar_genero(self):
        return ', '.join(genero.nombre for genero in self.genero.all()[:3])

    mostrar_genero.short_description = 'Genero'


class Ejemplar(models.Model):
    # Modelo que representa una copia especfica de una publicacion
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          help_text='Identificador unico para este ejemplar')
    publicacion = models.ForeignKey(Publicacion,
                                    on_delete=models.RESTRICT, null=True)
    impresion = models.CharField(max_length=200)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    prestado_a = models.ForeignKey(User,
                                   on_delete=SET_NULL,
                                   null=True,
                                   blank=True
                                   )

    history = HistoricalRecords(bases=[IPAddressHistoricalModel, ])

    ESTADOS = (
        ('m', 'Mantenimiento'),
        ('p', 'Prestado'),
        ('d', 'Disponible'),
        ('r', 'Reservado'),
        ('x', 'Solo consulta'),
    )

    disponibilidad = models.CharField(
        max_length=1,
        choices=ESTADOS,
        blank=True,
        default='m',
        help_text='Disponibilidad de este ejemplar',
    )

    class Meta:
        verbose_name = ("Ejemplar")
        verbose_name_plural = ("Ejemplares")
        ordering = ['fecha_vencimiento']
        permissions = (("puede_marcar_devolucion",
                       "Aplicar devolucion de Ejemplar"),
                       ("puede_ver_prestamos",
                       "Ver todos los prestamos"),
                       )

    def __str__(self):
        return f'{self.id} ({self.publicacion.titulo})'

    def mostrar_titulo(self):
        return self.publicacion.titulo

    mostrar_titulo.short_description = 'Titulo'

    @property
    def ya_vencido(self):
        if self.fecha_vencimiento and date.today() > self.fecha_vencimiento:
            return True
        return False
