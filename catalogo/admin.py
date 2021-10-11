from django.contrib import admin
from .models import Autor, Genero, Idioma, Tipo, Publicacion, Ejemplar


admin.site.register(Genero)
admin.site.register(Idioma)
admin.site.register(Tipo)


class EjemplarInline(admin.TabularInline):
    model = Ejemplar
    readonly_fields = ['id']


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'mostrar_genero')
    inlines = [EjemplarInline]


class PublicacionInline(admin.TabularInline):
    model = Publicacion
    fields = ['titulo', 'isbn', 'genero', 'idioma', 'tipo', 'descripcion']


@admin.register(Ejemplar)
class EjemplarAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ('mostrar_titulo',
                    'disponibilidad',
                    'prestado_a',
                    'fecha_vencimiento',
                    'id')
    list_filter = (
        'disponibilidad',
        'prestado_a',
        'fecha_vencimiento')
    fieldsets = (
        ('Detalles del ejemplar', {
            'fields': ('publicacion',
                       'impresion',
                       'id')
        }),
        ('Disponibilidad', {
            'fields': ('disponibilidad',
                       'prestado_a',
                       'fecha_vencimiento')
        }),
    )


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombres', 'fecha_nacimiento', 'fecha_muerte')
    fields = ['nombres', 'apellidos', ('fecha_nacimiento', 'fecha_muerte')]

    inlines = [PublicacionInline]
