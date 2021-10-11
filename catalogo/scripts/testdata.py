# python manage.py runscript catalogo.scripts.testdata

from catalogo.models import Autor, Ejemplar, Genero, Idioma, Publicacion, Tipo

from django.contrib.auth import get_user_model

User = get_user_model()


def run():
    # o = Genero.objects.create(nombre="Narrativa")
    # o = Genero.objects.create(nombre="Lirica")
    # o = Genero.objects.create(nombre="Ensayo")
    # o = Genero.objects.create(nombre="Novela")
    # o = Genero.objects.create(nombre="Fantasia")
    # o.save()

    # o = Tipo.objects.create(nombre="Libro")
    # o = Tipo.objects.create(nombre="Folleto")
    # o = Tipo.objects.create(nombre="Revista")
    # o = Tipo.objects.create(nombre="Manual")
    # o = Tipo.objects.create(nombre="Manuscrito")
    # o.save()

    # o = Idioma.objects.create(nombre="Espanol")
    # o = Idioma.objects.create(nombre="Ingles")
    # o = Idioma.objects.create(nombre="Frances")
    # o = Idioma.objects.create(nombre="Latin")
    # o = Idioma.objects.create(nombre="Griego")
    # o.save()

    # a = Autor.objects.create(
    #     nombres='Anton Szandor',
    #     apellidos='LaVey',
    # )
    # a = Autor.objects.create(
    #     nombres='Patrick',
    #     apellidos='Rothfuss',
    #     fecha_nacimiento='1973-06-06',
    # )
    # a = Autor.objects.create(
    #     nombres='Abdul',
    #     apellidos='Alhazred',
    # )
    # a = Autor.objects.create(
    #     nombres='Neil',
    #     apellidos='Gaiman',
    #     fecha_nacimiento='1960-11-10',
    # )
    # a = Autor.objects.create(
    #     nombres='Gabriel',
    #     apellidos='Garcia Marquez',
    #     fecha_nacimiento='1927-03-06',
    #     fecha_muerte='2014-04-17',
    # )
    # a.save()

    # o = Publicacion.objects.create(
    #     titulo="Cronica de Una Muerte Anunciada",
    #     descripcion="Novela publicada en 1981",
    #     isbn="000-111-222",
    # )
    # o.save()

    # a = Autor.objects.get(pk=1)
    # o = Publicacion.objects.create(
    #     titulo="The Devil's Notebook",
    #     descripcion="It includes a foreword by Adam Parfrey and design by Sean Tejaratchi",
    #     isbn="0-922915-11-3",
    # )

    # a = Autor.objects.get(pk=2)
    # o = Publicacion.objects.create(
    #     titulo="The Name of the Wind",
    #     descripcion="Magic and school loans",
    #     isbn="978-0-7564-0407-9",
    # )
    # o.autor = a
    # i = Idioma.objects.get(pk=2)
    # o.idioma = i
    # g = Genero.objects.get(pk=1)
    # o.genero.add(g)
    # g = Genero.objects.get(pk=4)
    # o.genero.add(g)
    # g = Genero.objects.get(pk=5)
    # o.genero.add(g)
    # t = Tipo.objects.get(pk=1)
    # o.tipo.add(t)
    # o.save()

    # o = Publicacion.objects.create(
    #     titulo="The Wise Man's Fear",
    #     descripcion="More magic and court drama",
    #     isbn="978-0-7564-0473-4",
    # )
    # o.autor = a
    # o.idioma = i
    # g = Genero.objects.get(pk=1)
    # o.genero.add(g)
    # g = Genero.objects.get(pk=4)
    # o.genero.add(g)
    # g = Genero.objects.get(pk=5)
    # o.genero.add(g)
    # o.tipo.add(t)
    # o.save()

    # a = Autor.objects.get(pk=2)
    # o = Publicacion.objects.create(
    #     titulo="The Slow Regard of Silent Things",
    #     descripcion="Auri's adventures in the Underthing",
    #     isbn="978-0-7564-1043-8",
    # )
    # o.autor = a
    # i = Idioma.objects.get(pk=2)
    # o.idioma = i
    # g = Genero.objects.get(pk=1)
    # o.genero.add(g)
    # g = Genero.objects.get(pk=2)
    # o.genero.add(g)
    # g = Genero.objects.get(pk=5)
    # o.genero.add(g)
    # t = Tipo.objects.get(pk=1)
    # o.tipo.add(t)
    # o.save()

    # p = Publicacion.objects.get(pk=3)
    # o = Ejemplar.objects.create(
    #     impresion="Tercera edicion, Pasta dura",
    #     disponibilidad='m',
    # )
    # o.publicacion = p
    # o.save()

    # o = Ejemplar.objects.create(
    #     impresion="Primera edicion, Pasta dura",
    #     disponibilidad='r',
    # )
    # o.publicacion = p
    # u = User.objects.get(pk=3)
    # o.prestado_a = u
    # o.save()

    # o = Ejemplar.objects.create(
    #     impresion="Segunda edicion, rustica",
    #     disponibilidad='p',
    #     fecha_vencimiento='2021-10-30'
    # )
    # o.publicacion = p
    # u = User.objects.get(pk=2)
    # o.prestado_a = u
    # o.save()

    o = Ejemplar.objects.get(pk="12a52ef2-f60d-4f50-a6dd-a4f7e792149c")
    o.delete()

    # print(g)  # a, g, i, t)
