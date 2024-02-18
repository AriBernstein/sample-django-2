# sample-django-2
Following the official Django First App tutorial


access Docker file system for Django app
```
docker exec -t -i django /bin/bash
```

update after change to model
```
docker exec -t -i django /bin/bash -c "python3 manage.py makemigrations ; python3 manage.py migrate"
```

python3.10 -m venv venv
. venv/bin/activate
pip3 install django
django-admin startproject pollsproject
cd pollsproject 
python3 manage.py startapp pollsapp
python3 manage.py runserver