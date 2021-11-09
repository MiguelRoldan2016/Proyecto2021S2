import datetime
from django import forms
from django.core.exceptions import ValidationError

from .models import Ejemplar, Autor


class NewLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    fotoData = forms.CharField(widget=forms.HiddenInput(),
                               required=False)


class AutorModelForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'placeholder': 'AAAA-MM-DD'}),
    )
    fecha_muerte = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'placeholder': 'AAAA-MM-DD'}),
    )

    class Meta:
        model = Autor
        fields = ('nombres',
                  'apellidos',
                  'fecha_nacimiento',
                  'fecha_muerte',
                  'imagen',
                  )


class RenovarPrestamoModelForm(forms.ModelForm):
    fecha_vencimiento = forms.DateField(widget=forms.SelectDateWidget())

    def clean_fecha_vencimiento(self):
        data = self.cleaned_data['fecha_vencimiento']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(
                "Fecha incorrecta - renovacion en el pasado")

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(
                "Fecha incorrecta - renovacion excede cuatro semanas")

        # Remember to always return the cleaned data.
        return data

    class Meta:
        model = Ejemplar
        fields = ['fecha_vencimiento']
        labels = {'fecha_vencimiento': "Fecha de vencimiento"}
        help_texts = {'fecha_vencimiento':
                      "Maximo cuatro semanas despues de hoy"}


class EjemplarModelForm(forms.ModelForm):
    fecha_inicio = forms.DateField(
        initial=datetime.date.today,
        disabled=True)
    fecha_vencimiento = forms.DateField(
        initial=datetime.date.today() + datetime.timedelta(weeks=4))

    class Meta:
        model = Ejemplar
        fields = (
            'fecha_inicio',
            'fecha_vencimiento',
        )
