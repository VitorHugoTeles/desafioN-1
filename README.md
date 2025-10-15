# desafioN-1

API RESTful de gerenciamento de usuários construída com Django e Django Rest Framework
utilizado python 3.12
ambiente virtual : conda
banco de dados: sqlite3

## 3. Instalação e Configuração

1.  **Clone o Repositório:**
    ```bash
    git clone git@github.com:VitorHugoTeles/desafioN-1.git
    cd desafioN-1/mysite
    ```
2.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate 
    ```
3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Execute as Migrações:**
    ```bash
    python manage.py migrate
    ```
5.  **Crie um Superusuário (para acesso ao Admin):**
    ```bash
    python manage.py createsuperuser
    ```
6.  **Execute o Servidor:**
    ```bash
    python manage.py runserver
    ```

Acesso:

    API Root: http://127.0.0.1:8000/api/usuario/

    Admin: http://127.0.0.1:8000/admin/  
