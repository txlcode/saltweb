vhost_conf:
  file.managed:
    - name: /etc/nginx/conf.d/vhost.conf
    - source: salt://nginx_yum/file/test_vhost.conf
    - user: root
    - group: root
    - mode: 644
