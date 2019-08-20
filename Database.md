## 1.数据库操作指南

使用Django框架会遇见最基本的数据库相关的操作，我们把典型的数据库操作做一些必要的介绍。



## 2.数据库表生成
```python
python manage.py migrate
python manage.py makemigrations
manage.py showmigrations
manage.py migrate polls 0004 --fake
```


## 3.创建Django Admin的root管理员用户
```python
python manage.py createsuperuser
```

## 4.修改root用户的管理员密码
```python
python manage.py changepassword
```


## 5.交互命令行的方式进入Django的上线文环境
```python
python manage.py shell
```


## 6.修改指定名称用户的密码

```python
python manage.py shell
from django.contrib.auth.models import User
user =User.objects.get(username='admin')
user.set_password('new_password')
user.save()
```

## 7. Django ORM插入操作

这是一个数据插入的Django ORM展示，之后复杂的操作也是基于简单操作的变型。

使用的Django Command调用models数据库类操作，是不用启动WEB服务器的，Django ORM就可以独立完成数据的操作。之后数据插入功能的数据源可能来源于各种数据源形式，不一定只能是HTTP WEB监听一种方式。


```python 
from sidecar.models import cmdb,testcase
max_id = testcase.objects.all().order_by("-id")[0]
new_maxid = max_id.id + 1
testcase.objects.create(id=(max_id.id + 1),name1="a", name2="b", name3="c")
```

