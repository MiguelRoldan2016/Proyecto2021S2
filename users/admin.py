from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

# admin.site.register(Group)


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['email', 'is_staff', 'is_superuser', 'is_active']
    list_filter = ['is_staff']
    add_fieldsets = (
        (None, {'fields': ('email', 'password', 'password_2')}),
        ('Datos personales', {
         'fields': ('nombres', 'apellidos', 'edad', 'foto')}),
        ('Privilegios', {'fields': ('is_staff', 'is_superuser')}),
        ('Grupos de acceso', {'fields': ('groups', )})
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Datos personales', {
         'fields': ('nombres', 'apellidos', 'edad', 'foto')}),
        ('Privilegios', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Grupos de acceso', {'fields': ('groups', )})
    )

    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
