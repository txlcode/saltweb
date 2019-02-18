nginx_conf:
  file.managed:
    - name: /opt/nginx/conf/nginx.conf
    - source: salt://nginx/conf/nginx.j2
    - template: jinja
nginx_service:
  file.managed:
    - name: /usr/lib/systemd/system/nginx.service
    - user: root
    - mode: 755
    - source: salt://nginx/files/nginx.service
  cmd.run:
    - names:
      - /usr/bin/systemctl daemon-reload
      - /usr/bin/systemctl enable nginx
  service.running:
    - name: nginx
    - enable: True
    - watch:
      - file: nginx_conf
