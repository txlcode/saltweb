# SOMS
https://github.com/qitan/SOMS

最好使用CENTOS7的python2.7
安装PIP（有的话不用装）

```
# wget https://bootstrap.pypa.io/get-pip.py
# python get-pip.py
# cat > /etc/pip.conf <<EOF
[global]
index-url = https://pypi.douban.com/simple
trusted-host = pypi.douban.com
disable-pip-version-check = true
timeout = 120
EOF
```
安装mysql模块
```
yum install gcc python-devel mysql-devel  MySQL-python -y
```


配置salt-api

```
# pip install pyOpenSSL==16.2.0
# useradd -M -s /sbin/nologin saltapi && echo "password"|/usr/bin/passwd saltapi --stdin
# salt-call --local tls.create_self_signed_cert
```

配置salt-master
我这里把soms解压到了/data/wwwroot下

```
# cat > /etc/salt/master <<EOF
interface: 0.0.0.0

external_auth:
  pam:
    saltapi:
      - .*
      - '@wheel'
      - '@runner'
      - '@jobs'

rest_cherrypy:
  port: 8000
  ssl_crt: /etc/pki/tls/certs/localhost.crt
  ssl_key: /etc/pki/tls/certs/localhost.key

file_recv: True

include: /data/wwwroot/soms/saltconfig/*.conf
EOF
```

配置好后，把服务启起来，并测试salt-api

```
##centos6
# service salt-master start
# service salt-api start
# service salt-minion start
##centos7
# systemctl start salt-master salt-api salt-minion
##
# curl -sSk https://localhost:8000/login -H 'Accept: application/x-yaml' -d username=saltapi -d password=password -d eauth=pam
```

返回如下信息则配置成功：

```
return:
- eauth: pam
  expire: 1472695867.308063
  perms:
  - .*
  - '@wheel'
  - '@runner'
  - '@jobs'
  start: 1472652667.308062
  token: 99993ca778fa4f31dce472421cbf01d37be936ad
  user: saltapi
```

上面这些操作都完成后就可以部署soms项目了

安装依赖(组件要求查看requirements.txt)

```
# pip install -r requirements.txt
#1，修改soms/setting.py里面mysql的设置
#2，修改saltconfig/nodegroup.conf下mysql的设置
#3，修改soms/settings_local.py里面saltapi的设置
#4，修改deploy/views.py里面salt_flush_module.path 为salt文件存储的地方
```
同步salt日志到数据库

yum install epel-release
yum install supervisor
supervisord -c /data/wwwroot/soms/salt_event_to_mysql_supervisord.conf

同步数据库

```
# python manage.py makemigrations
# python manage.py migrate
```

创建管理员

```
# python manage.py createsuperuser
```

runserver运行检查是否正常

```
# python manage.py runserver 0.0.0.0:8080
如果有uwsgi，就不用运行上面的语句。

如果无法正常运行，请检查以上步骤  

20180201新增:  
新增file_bakup.py文件，放至项目下media/salt/_modules目录下，然后执行如下命令同步到minion  
salt '*' saltutil.sync_all

20170721新增：  
关于部署完后报401错误的，需要修改soms/settings_local.py里的相关信息

有任何问题或指教可加QQ群或在本人博客留言  
QQ群：291809453  
爱猫家 https://imaojia.com    
或者email：qqing_lai@hotmail.com  

PS:

  soms正常运行后，正式上线最好部署django+nginx+uwsgi环境  
  https://imaojia.com/blog/linux/django-nginx-uwsgi-setup-on-centos


代码写的比较烂，欢迎吐槽 -_-||

