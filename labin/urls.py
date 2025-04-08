from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Minha API",
        default_version="v1",
        description="Descrição da API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contato@exemplo.com"),
        license=openapi.License(name="Licença BSD"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    # Redoc (documentação alternativa)
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # JSON/YAML para Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # Rotas do sistema
    path('admin/', admin.site.urls),
    path('agendamento/', include('agendamento.urls')),
    path('auth/', include('usuarios.urls')),
]
