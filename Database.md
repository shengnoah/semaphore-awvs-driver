## 1.数据库操作指南

使用Django框架会遇见最基本的数据库相关的操作，我们把典型的数据库操作做一些必要的介绍。



## 2.数据库表生成
python manage.py migrate
python manage.py makemigrations
manage.py showmigrations
manage.py migrate polls 0004 --fake


## 3.创建Django Admin的root管理员用户
python manage.py createsuperuser

## 4.修改root用户的管理员密码
python manage.py changepassword


## 5.交互命令行的方式进入Django的上线文环境
python manage.py shell


## 6.修改指定名称用户的密码

python manage.py shell
from django.contrib.auth.models import User
user =User.objects.get(username='admin')
user.set_password('new_password')
user.save()
