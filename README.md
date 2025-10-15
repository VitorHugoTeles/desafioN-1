# desafioN-1

API RESTful de gerenciamento de usuários construída com Django e Django Rest Framework
utilizado python 3.12
ambiente virtual : conda
banco de dados: sqlite3

instalação 
no terminal digite:
  git clone https://github.com/VitorHugoTeles/desafioN-1.git
  cd desafioN-1/mysite
  python -m venv .venv
  source .venv/bin/activate  # No Linux/macOS
  # .venv\Scripts\activate   # No Windows
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py createsuperuser
  python manage.py runserver

Acesso:

    API Root: http://127.0.0.1:8000/api/usuario/

    Admin: http://127.0.0.1:8000/admin/  
