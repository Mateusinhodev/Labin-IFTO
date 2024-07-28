from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name= 'home'),
    path('ver_agendamento/<int:id>', views.ver_agendamento, name= 'ver_agendamento'),
    path('agendamento_aula', views.agendamento_aula, name='agendamento_aula')
]
