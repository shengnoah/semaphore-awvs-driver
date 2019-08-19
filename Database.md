


python manage.py migrate
python manage.py makemigrations

python manage.py createsuperuser
manage.py showmigrations

manage.py migrate polls 0004 --fake





python manage.py shell

from django.contrib.auth.models import User

user =User.objects.get(username='admin')

user.set_password('new_password')

user.save()


python manage.py createsuperuser


python manage.py changepassword


