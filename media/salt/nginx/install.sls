nginx_source:
  file.managed:
    - unless: test -f /usr/local/src/nginx-1.14.0-mian_anzhuang.tar.gz
    - name: /usr/local/src/nginx-1.14.0-mian_anzhuang.tar.gz
    - source: salt://nginx/bags/nginx-1.14.0-mian_anzhuang.tar.gz
    - user: root
    - group: root
    - mode: 644
install_soft:
  pkg.installed:
    - names:
      - gcc
nginx_user:
  user.present:
    - name: nginx
    - createhome: False
    - shell: /sbin/nologin
extract_nginx:
  cmd.run:
    - unless: test -d /opt/nginx-1.14.0/
    - cwd: /usr/local/src
    - names :
      - tar zxvf nginx-1.14.0-mian_anzhuang.tar.gz -C /opt && chown nginx:nginx -R /opt/nginx-1.14.0 && ln -s /opt/nginx-1.14.0 /opt/nginx &&  mkdir -p /data/logs/nginx && chmod 777 -R /data/logs 
    - require:
      - file: nginx_source
