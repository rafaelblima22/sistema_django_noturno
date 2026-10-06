from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('novoPaciente/', views.novoPaciente, name='novo-paciente'),
    path('novoPacienteSucesso/', views.novo_paciente_sucesso, name='novo-paciente-sucesso'),
]