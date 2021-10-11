from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm

from .models import User

User = get_user_model()


class RegisterForm(UserCreationForm):
    """ Formulario de registro """
    email = forms.EmailField(max_length=254,
                             help_text="Correo electronico",
                             )
    password1 = forms.CharField(label="Contrasena",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contrasena",
                                widget=forms.PasswordInput)
    nombres = forms.CharField(max_length=100,
                              initial="",
                              widget=forms.TextInput(attrs={
                                  'placeholder': 'Nombre(s) del usuario'
                              }))
    apellidos = forms.CharField(max_length=100,
                                initial="",
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Apellido(s) del usuario'
                                }))
    edad = forms.IntegerField(initial=None)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2',
                  'nombres', 'apellidos', 'edad']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Esta direccion de correo ya existe")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password is not None and password != password2:
            self.add_error('password2', "Las contrasenas no coinciden")
        return cleaned_data


class UserAdminCreationForm(forms.ModelForm):
    """ Formulario para crear usuarios nuevos """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(widget=forms.PasswordInput,
                                 label="Confirmar contrasena")

    class Meta:
        model = User
        fields = ['email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Las contrasenas no coinciden")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """ Formulario para actualizar usuarios """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'password', 'is_active', 'is_staff']

    def clean_password(self):
        return self.initial["password"]
