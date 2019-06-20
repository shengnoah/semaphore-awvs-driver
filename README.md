

"互联网公司的一项趋势为逐步将安全集成到其SDLC（系统安全开发生命周期）中。安全团队逐步使用商业、开源工具设定合理的安全策略，尝试自动化发现漏洞，帮助开发团队快速定位修复代码，节省公司宝贵的开发和安全团队时间、人力资源，降低修复成本。该工具所解决的痛点为当前敏捷活动中依靠纯人力的安全评估已经不能满足业务快速发展，开源实现一套系统实现核心调度机制，持续通过对应用层进行黑白盒审计，基本实现最大化利用工具自动化发现漏洞；未来长期价值在于实现落地SDL能力、对业务线进行安全赋能，保护公司应用、数据的风险也得以最小化。"

## 维护者

[tomwilson28](https://github.com/tomwilson28)

[shengnoah](https://github.com/shengnoah)

# 1.安装依赖包 

```
# 安装虚拟环境
sudo pip install virtualenv
sudo pip install virtualenvwrapper  --upgrade --ignore-installed

# .bash_profile
source /usr/local/bin/virtualenvwrapper.sh

# 创建Python环境
mkvirtualenv py27 -p /usr/bin/python
workon py27

# 安装Django框架
pip install django==1.11.15

# 安装Django REST
pip install djangorestframework==3.8.2

# 安装Django RPC
git clone git://github.com/samuraisam/django-json-rpc.git
cd django-json-rpc
python setup.py install

# 安装基础HTTP库
pip install reqeusts

# 安装pytest库
pip install pytest
```

# 2.创建Django工程
```
django-admin startproject wvs
```

# 3.创建Django APP

```
django-admin startapp scanner
```

# 4.环境部署 

Add 'jsonrpc' to your INSTALLED_APPS in your settings.py file
设置Django RPC server，端口为5000

# 5.RPC方法声明

```python
from jsonrpc import jsonrpc_method
@jsonrpc_method('myapp.sayHello')
def whats_the_time(request, name='Lester'):
  return "Hello %s" % name
```

# 6.RPC方法调用
```python
from jsonrpc.proxy import ServiceProxy
s = ServiceProxy('http://localhost:5000/json/')
s.myapp.sayHello('Sam') 
```

# 7.Django Command测试
```python
python manage.py dsl
```

显示semaphore/wvs/cmd/management/commands/dsl.pyc执行成功, 参数为close则为成功

# 8.pytest测试

```
pytest -v -s -m"scan" test.py
```

# 9.文档生成


```
npm install -g mermaid.cli
dot arch.dot -T png -o arch.png
```

# 10. REST接口测试
```
curl -l -H "Content-type: application/json" -X POST -d '{"key":"test","domain":"test.com","index":"index.php","file":"index.php","params":"key1,key2,key3", "source":"test", "content":"test"}'  127.0.0.1:5000/interface_update/
```

### sidecar
```
curl -l -H "Content-type: application/json" -X POST -d '{"key":"test","domain":"test.com","index":"index.php","file":"index.php","params":"key1,key2,key3", "source":"test", "content":"test"}'  127.0.0.1:5000/sidecar/
```


# 11. 创建Admin数据库
```python
python manage.py migrate
python manage.py makemigrations
manage.py makemigrations && manage.py migrate
python manage.py createsuperuser
manage.py showmigrations
manage.py migrate polls 0004 --fake
```


# 12. 部署方式

```python
#12.1.启动REST API服务
python manage.py runserver 0.0.0.0:8080

#12.2.启动RPC服务。 
python manage.py runserver 0.0.0.0:5000

#12.3.测试时序调用。

#12.3.1 测试能过REST API调用RPC。
curl -l -H "Content-type: application/json" -X POST -d '{"key":"test","domain":"test.com","index":"index.php","file":"index.php","params":"key1,key2,key3", "source":"test", "content":"test"}'  127.0.0.1:5000/interface_update/

# 12.3.2 测试直接调用RPC。
curl -l -H "Content-type: application/json" -X POST -d '{"key":"test","domain":"test.com","index":"index.php","file":"index.php","params":"key1,key2,key3", "source":"test", "content":"test"}'  127.0.0.1:5000/sidecar/
```


