from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agendamento/', include('agendamento.urls')),
    path('auth/', include('usuarios.urls'))
] 