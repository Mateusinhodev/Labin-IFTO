# Sistema de Controle de Acesso aos Laboratórios - IFTO Campus Colinas

Este é um sistema web desenvolvido para gerenciar o controle de acesso aos laboratórios da faculdade IFTO Campus Colinas. O sistema permite agendar o uso dos laboratórios, registrar horários e monitorar o acesso dos usuários. O projeto foi desenvolvido utilizando **Python** e o framework **Django**, contando também com uma API para integração com outros sistemas.

## Funcionalidades

- **Cadastro de usuários**: Permite o registro de usuários, como adminitrador do sistema.
- **Agendamento de Laboratórios**: Adminitrador do sistema pode agendar o uso dos laboratórios, especificando qual o laboratório desejável, o nome professor, data e horário de inicio e fim de aula .
- **Monitoramento de Acessos**: Registra os acessos aos laboratórios para controle e segurança.
- **API REST**: Disponibiliza uma API para integrar o sistema com outras plataformas e aplicativos.

## Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada no backend.
- **Django**: Framework web utilizado para desenvolver o sistema.
- **Django Rest Framework (DRF)**: Utilizado para a criação da API.
- **SQLite**  Banco de dados para armazenar os dados do sistema.
- **Bootstrap**: Framework CSS para tornar a interface responsiva.

## Requisitos

- Python 
- Django
- Django Rest Framework
- Banco de dados SQLite

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/Mateusinhodev/Labin-IFTO.git
    cd Labin-IFTO
    ```

2. Crie e ative um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate  # Para Windows
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Realize as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

## Uso da API

A API oferece endpoints para o controle de agendamentos e acessos aos laboratórios. Ela pode ser utilizada para integrar o sistema a outras plataformas.

### Exemplos de Endpoints

- `GET /agendamento/agendamentos/`: Cria um novo agendamento de laboratório.
- `GET /api/agendamentos/id/`: Detalha um agendamento específico.