from django.urls import path
from . import views
from forms import CustomAuthForm

urlpatterns = [
    path('', views.LoginView.as_view(), name='oldlogin'),
    path('logout', views.logout_view, name='logout'),
]
