Para rodar o projeto localmente é necessário ter Python instalado em sua máquina 
```
https://www.python.org/downloads/
```
e então, instalar Django no terminal através do sistema de gerenciamento de pacotes padrão do Python
```
pip install Django
```
na pasta Sistema, fazer as migrações do banco de dados 
```
python manage.py migrate
```
criar um superuser, necessário para poder fazer login no sistema
```
python manage.py createsuperuser
```
e então, rodar o servidor de desenvolvimento localmente
```
python manage.py runserver
```
