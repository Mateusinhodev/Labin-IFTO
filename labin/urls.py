from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agendamento/', include('agendamento.urls')),
    path('auth/', include('usuarios.urls'))
] 
