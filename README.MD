# Arquitetura do DJANGO

## Criar venv
    > python -m venv venv

## Ativar venv 
    > .\venv\Scripts\Activate

## Selecionar interpretador
    -> CTRL/SHIFT/P
    -> Pesquisar por: "python select" e selecione a que tem nossa venv e está marcada como "Recomendada"

## Instalar Django, Rest_Framework e Corsheaders
    

## API_ROOT
    + settings.py - Configurações gerais
    + urls.py - Linkar aplicação 

## API_REST
    + models.py - Criar modelos para o banco de dados
    + admin.py - Configurar edição de modelos (opcional)
    + serializers.py - Gerar JSON's dos modelos
    + views.py - Funções da API
    + urls.py - Linkar funções

### /settings.py
    + Adicionar ao INSTALLED_APPS
        + rest_framework
        + corsheaders
        + api_rest

    + Adicionar ao MIDDLEWARE
        + corsheaders.middleware.CorsMiddleware

    + Criar um CORS_ALLOW_ORIGINS
        CORS_ALLOW_ORIGINS = [
           'http://localhost:8000', 
        ]
        
        + Artenativa:
            + CORS_ORIGINS_ALLOW = True

### /models.py

### /admin.py
