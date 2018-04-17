#SGPF [Django]

##Instalación

###MyCash
    * sudo apt-get install python-pip
    * sudo pip install virtualenv
    * sudo apt-get install python-dev libpq-dev
    * mkdir Django
    * cd Django
    * virtualenv venv
    * source venv/bin/activate | deactivate
    * pip install django==1.9
    * django-admin.py --version
    * pip install psycopg2
    * django-admin.py startproject sgpf

###DataBase
    * modify database
    * python manage.py makemigrations
    * python manage.py migrate
    * python manage.py makemigrations mycash | models class