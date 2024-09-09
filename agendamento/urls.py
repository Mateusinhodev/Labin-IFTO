from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views 
from .views import AgendamentoViewSet

# Criando o roteador da API
router = DefaultRouter()
router.register(r'agendamentos', AgendamentoViewSet)

urlpatterns = [
    path('home/', views.home, name= 'home'),
    path('ver_agendamento/<int:id>', views.ver_agendamento, name= 'ver_agendamento'),
    path('agendamento_aula', views.agendamento_aula, name='agendamento_aula'),
    path('', include(router.urls))
]
