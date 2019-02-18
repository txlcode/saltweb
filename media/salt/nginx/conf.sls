nginx_conf:
  file.managed:
    - name: /opt/nginx/conf/nginx.conf
    - source: salt://nginx/conf/nginx.j2
    - template: jinja
nginx_service:
  file.managed:
    - name: /etc/init.d/nginx
    - user: root
    - mode: 755
    - source: salt://nginx/files/nginx
  cmd.run:
    - unless: /sbin/chkconfig --list nginx
    - names:
      - /sbin/chkconfig --add nginx
      - /sbin/chkconfig nginx on
  service.running:
    - name: nginx
    - enable: True
    - watch:
      - file: nginx_conf
