redis-master-config:
  file.managed:
    - name: /etc/redis.conf
    - source: salt://redis_yum/conf/redis-master.conf
    - user: root
    - group: root
    - mode: 644
    - template: jinja
    - defaults:
      REDIS_MEM: 1G

redis-master-service:
  service.running:
    - name: redis
    - enable: True
    - watch:
      - file: redis-master-config
